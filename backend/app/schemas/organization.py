from typing import Any, Optional
from uuid import UUID

from pydantic import BaseModel, Field

from app.schemas.common import EntityRead


class OrganizationCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    slug: str = Field(..., min_length=1, max_length=120)
    description: Optional[str] = None
    settings: dict[str, Any] = Field(default_factory=dict)


class OrganizationUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=120)
    description: Optional[str] = None
    settings: Optional[dict[str, Any]] = None


class OrganizationRead(EntityRead):
    name: str
    slug: str
    description: Optional[str] = None
    settings: dict[str, Any]


class DepartmentCreate(BaseModel):
    organization_id: UUID
    name: str = Field(..., min_length=1, max_length=120)
    description: Optional[str] = None
    head_employee_id: Optional[UUID] = None


class DepartmentRead(EntityRead):
    organization_id: UUID
    name: str
    description: Optional[str] = None
    head_employee_id: Optional[UUID] = None


class TeamCreate(BaseModel):
    department_id: UUID
    name: str = Field(..., min_length=1, max_length=120)
    mission: Optional[str] = None
    lead_employee_id: Optional[UUID] = None


class TeamRead(EntityRead):
    department_id: UUID
    name: str
    mission: Optional[str] = None
    lead_employee_id: Optional[UUID] = None


class EmployeeCreate(BaseModel):
    team_id: UUID
    manager_id: Optional[UUID] = None
    name: str = Field(..., min_length=1, max_length=120)
    role: str = Field(..., min_length=1, max_length=80)
    seniority: str = Field(default="senior", max_length=40)
    model_provider: str = Field(default="openai", max_length=64)
    model_name: str = Field(default="gpt-4o", max_length=120)
    system_prompt: Optional[str] = None
    capabilities: list[str] = Field(default_factory=list)


class EmployeeRead(EntityRead):
    team_id: UUID
    manager_id: Optional[UUID] = None
    name: str
    role: str
    seniority: str
    status: str
    model_provider: str
    model_name: str
    system_prompt: Optional[str] = None
    capabilities: list[str]
