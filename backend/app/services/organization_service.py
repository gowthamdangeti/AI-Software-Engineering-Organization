from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.organization import Department, Employee, Organization, Team
from app.repositories.organization import (
    DepartmentRepository,
    EmployeeRepository,
    OrganizationRepository,
    TeamRepository,
)
from app.schemas.organization import (
    DepartmentCreate,
    EmployeeCreate,
    OrganizationCreate,
    TeamCreate,
)


class OrganizationService:
    """Business logic for organizations, departments, teams, and AI employees."""

    def __init__(self, session: AsyncSession) -> None:
        self.orgs = OrganizationRepository(session)
        self.departments = DepartmentRepository(session)
        self.teams = TeamRepository(session)
        self.employees = EmployeeRepository(session)

    async def list_organizations(self, *, limit: int = 50, offset: int = 0) -> tuple[list[Organization], int]:
        return await self.orgs.list_all(limit=limit, offset=offset)

    async def get_organization(self, organization_id: UUID) -> Organization:
        org = await self.orgs.get_by_id(organization_id)
        if org is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organization not found")
        return org

    async def create_organization(self, payload: OrganizationCreate) -> Organization:
        existing = await self.orgs.get_by_slug(payload.slug)
        if existing is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Organization slug '{payload.slug}' already exists",
            )
        return await self.orgs.create(**payload.model_dump())

    async def list_departments(self, organization_id: UUID) -> list[Department]:
        await self.get_organization(organization_id)
        return await self.departments.list_by_organization(organization_id)

    async def create_department(self, payload: DepartmentCreate) -> Department:
        await self.get_organization(payload.organization_id)
        return await self.departments.create(**payload.model_dump())

    async def list_teams(self, department_id: UUID) -> list[Team]:
        dept = await self.departments.get_by_id(department_id)
        if dept is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
        return await self.teams.list_by_department(department_id)

    async def create_team(self, payload: TeamCreate) -> Team:
        dept = await self.departments.get_by_id(payload.department_id)
        if dept is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
        return await self.teams.create(**payload.model_dump())

    async def list_employees(self, team_id: UUID) -> list[Employee]:
        team = await self.teams.get_by_id(team_id)
        if team is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team not found")
        return await self.employees.list_by_team(team_id)

    async def create_employee(self, payload: EmployeeCreate) -> Employee:
        team = await self.teams.get_by_id(payload.team_id)
        if team is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team not found")
        return await self.employees.create(**payload.model_dump())
