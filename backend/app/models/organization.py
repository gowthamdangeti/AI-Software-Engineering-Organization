import uuid
from typing import Optional

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin, UUIDPrimaryKeyMixin


class Organization(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Top-level virtual software engineering organization."""

    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(String(120), nullable=False)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    settings: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)

    departments: Mapped[list["Department"]] = relationship(
        back_populates="organization",
        cascade="all, delete-orphan",
    )
    projects: Mapped[list["Project"]] = relationship(
        back_populates="organization",
        cascade="all, delete-orphan",
    )


class Department(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Engineering department within an organization."""

    __tablename__ = "departments"

    organization_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("organizations.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    head_employee_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        nullable=True,
    )

    organization: Mapped["Organization"] = relationship(back_populates="departments")
    teams: Mapped[list["Team"]] = relationship(
        back_populates="department",
        cascade="all, delete-orphan",
    )


class Team(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Cross-functional or specialized engineering team within a department."""

    __tablename__ = "teams"

    department_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("departments.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    mission: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    lead_employee_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        nullable=True,
    )

    department: Mapped["Department"] = relationship(back_populates="teams")
    employees: Mapped[list["Employee"]] = relationship(
        back_populates="team",
        cascade="all, delete-orphan",
    )


class Employee(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Independent AI employee with role, reporting line, and model configuration."""

    __tablename__ = "employees"

    team_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("teams.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    manager_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("employees.id", ondelete="SET NULL"),
        nullable=True,
    )
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[str] = mapped_column(String(80), nullable=False)
    seniority: Mapped[str] = mapped_column(String(40), default="senior", nullable=False)
    status: Mapped[str] = mapped_column(String(32), default="idle", nullable=False)
    model_provider: Mapped[str] = mapped_column(String(64), default="openai", nullable=False)
    model_name: Mapped[str] = mapped_column(String(120), default="gpt-4o", nullable=False)
    system_prompt: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    capabilities: Mapped[list] = mapped_column(JSONB, default=list, nullable=False)

    team: Mapped["Team"] = relationship(back_populates="employees")
    manager: Mapped[Optional["Employee"]] = relationship(
        remote_side="Employee.id",
        backref="direct_reports",
    )
