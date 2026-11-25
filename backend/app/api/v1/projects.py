from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.common import PaginatedResponse
from app.schemas.project import (
    ProjectCreate,
    ProjectRead,
    TaskCreate,
    TaskRead,
    WorkflowCreate,
    WorkflowRead,
)
from app.services.project_service import ProjectService

router = APIRouter(tags=["Projects"])


def get_project_service(db: AsyncSession = Depends(get_db)) -> ProjectService:
    return ProjectService(db)


@router.get("/projects", response_model=PaginatedResponse[ProjectRead])
async def list_projects(
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    service: ProjectService = Depends(get_project_service),
) -> PaginatedResponse[ProjectRead]:
    items, total = await service.list_projects(limit=limit, offset=offset)
    return PaginatedResponse(items=items, total=total, limit=limit, offset=offset)


@router.post("/projects", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
async def create_project(
    payload: ProjectCreate,
    service: ProjectService = Depends(get_project_service),
) -> ProjectRead:
    return await service.create_project(payload)


@router.get("/projects/{project_id}", response_model=ProjectRead)
async def get_project(
    project_id: UUID,
    service: ProjectService = Depends(get_project_service),
) -> ProjectRead:
    return await service.get_project(project_id)


@router.get("/projects/{project_id}/tasks", response_model=list[TaskRead])
async def list_tasks(
    project_id: UUID,
    service: ProjectService = Depends(get_project_service),
) -> list[TaskRead]:
    return await service.list_tasks(project_id)


@router.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(
    payload: TaskCreate,
    service: ProjectService = Depends(get_project_service),
) -> TaskRead:
    return await service.create_task(payload)


@router.get("/projects/{project_id}/workflows", response_model=list[WorkflowRead])
async def list_workflows(
    project_id: UUID,
    service: ProjectService = Depends(get_project_service),
) -> list[WorkflowRead]:
    return await service.list_workflows(project_id)


@router.post("/workflows", response_model=WorkflowRead, status_code=status.HTTP_201_CREATED)
async def create_workflow(
    payload: WorkflowCreate,
    service: ProjectService = Depends(get_project_service),
) -> WorkflowRead:
    return await service.create_workflow(payload)
