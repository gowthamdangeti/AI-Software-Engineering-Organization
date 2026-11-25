from datetime import datetime
from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel, ConfigDict

T = TypeVar("T")


class OrmSchema(BaseModel):
    """Base Pydantic schema configured for SQLAlchemy ORM objects."""

    model_config = ConfigDict(from_attributes=True)


class EntityRead(OrmSchema):
    """Base read schema with UUID identifier and timestamps."""

    id: UUID
    created_at: datetime
    updated_at: datetime


class PaginatedResponse(BaseModel, Generic[T]):
    """Standard paginated list response wrapper."""

    items: list[T]
    total: int
    limit: int
    offset: int
