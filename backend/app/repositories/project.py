from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Project, Task, Workflow
from app.repositories.base import BaseRepository


class ProjectRepository(BaseRepository[Project]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Project, session)

    async def list_by_organization(self, organization_id: UUID) -> list[Project]:
        stmt = select(Project).where(Project.organization_id == organization_id)
        return list((await self.session.execute(stmt)).scalars().all())


class TaskRepository(BaseRepository[Task]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Task, session)

    async def list_by_project(self, project_id: UUID) -> list[Task]:
        stmt = select(Task).where(Task.project_id == project_id)
        return list((await self.session.execute(stmt)).scalars().all())


class WorkflowRepository(BaseRepository[Workflow]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Workflow, session)

    async def list_by_project(self, project_id: UUID) -> list[Workflow]:
        stmt = select(Workflow).where(Workflow.project_id == project_id)
        return list((await self.session.execute(stmt)).scalars().all())
