from typing import Any, Optional
from uuid import UUID

from pydantic import BaseModel, Field

from app.schemas.common import EntityRead


class ProjectCreate(BaseModel):
    organization_id: UUID
    name: str = Field(..., min_length=1, max_length=160)
    description: Optional[str] = None
    repository_url: Optional[str] = Field(default=None, max_length=500)


class ProjectRead(EntityRead):
    organization_id: UUID
    name: str
    description: Optional[str] = None
    repository_url: Optional[str] = None
    status: str


class TaskCreate(BaseModel):
    project_id: UUID
    assignee_id: Optional[UUID] = None
    parent_task_id: Optional[UUID] = None
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    priority: int = Field(default=2, ge=1, le=5)
    extra_metadata: dict[str, Any] = Field(default_factory=dict)


class TaskRead(EntityRead):
    project_id: UUID
    assignee_id: Optional[UUID] = None
    parent_task_id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    status: str
    priority: int
    extra_metadata: dict[str, Any]


class WorkflowCreate(BaseModel):
    project_id: UUID
    name: str = Field(..., min_length=1, max_length=160)
    description: Optional[str] = None
    definition: dict[str, Any] = Field(default_factory=dict)


class WorkflowRead(EntityRead):
    project_id: UUID
    name: str
    description: Optional[str] = None
    status: str
    definition: dict[str, Any]
