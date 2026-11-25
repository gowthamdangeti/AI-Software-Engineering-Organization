from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Project, Task, Workflow
from app.repositories.organization import OrganizationRepository
from app.repositories.project import ProjectRepository, TaskRepository, WorkflowRepository
from app.schemas.project import ProjectCreate, TaskCreate, WorkflowCreate


class ProjectService:
    """Business logic for projects, tasks, and workflows."""

    def __init__(self, session: AsyncSession) -> None:
        self.orgs = OrganizationRepository(session)
        self.projects = ProjectRepository(session)
        self.tasks = TaskRepository(session)
        self.workflows = WorkflowRepository(session)

    async def list_projects(self, *, limit: int = 50, offset: int = 0) -> tuple[list[Project], int]:
        return await self.projects.list_all(limit=limit, offset=offset)

    async def get_project(self, project_id: UUID) -> Project:
        project = await self.projects.get_by_id(project_id)
        if project is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
        return project

    async def create_project(self, payload: ProjectCreate) -> Project:
        org = await self.orgs.get_by_id(payload.organization_id)
        if org is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organization not found")
        return await self.projects.create(**payload.model_dump())

    async def list_tasks(self, project_id: UUID) -> list[Task]:
        await self.get_project(project_id)
        return await self.tasks.list_by_project(project_id)

    async def create_task(self, payload: TaskCreate) -> Task:
        await self.get_project(payload.project_id)
        return await self.tasks.create(**payload.model_dump())

    async def list_workflows(self, project_id: UUID) -> list[Workflow]:
        await self.get_project(project_id)
        return await self.workflows.list_by_project(project_id)

    async def create_workflow(self, payload: WorkflowCreate) -> Workflow:
        await self.get_project(payload.project_id)
        return await self.workflows.create(**payload.model_dump())
