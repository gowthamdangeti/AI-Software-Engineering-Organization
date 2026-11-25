from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.organization import Department, Employee, Organization, Team
from app.repositories.base import BaseRepository


class OrganizationRepository(BaseRepository[Organization]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Organization, session)

    async def get_by_slug(self, slug: str) -> Optional[Organization]:
        stmt = select(Organization).where(Organization.slug == slug)
        return (await self.session.execute(stmt)).scalar_one_or_none()


class DepartmentRepository(BaseRepository[Department]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Department, session)

    async def list_by_organization(self, organization_id: UUID) -> list[Department]:
        stmt = select(Department).where(Department.organization_id == organization_id)
        return list((await self.session.execute(stmt)).scalars().all())


class TeamRepository(BaseRepository[Team]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Team, session)

    async def list_by_department(self, department_id: UUID) -> list[Team]:
        stmt = select(Team).where(Team.department_id == department_id)
        return list((await self.session.execute(stmt)).scalars().all())


class EmployeeRepository(BaseRepository[Employee]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Employee, session)

    async def list_by_team(self, team_id: UUID) -> list[Employee]:
        stmt = select(Employee).where(Employee.team_id == team_id)
        return list((await self.session.execute(stmt)).scalars().all())
