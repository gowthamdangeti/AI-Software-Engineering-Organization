from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.common import PaginatedResponse
from app.schemas.organization import (
    DepartmentCreate,
    DepartmentRead,
    EmployeeCreate,
    EmployeeRead,
    OrganizationCreate,
    OrganizationRead,
    TeamCreate,
    TeamRead,
)
from app.services.organization_service import OrganizationService

router = APIRouter(tags=["Organization"])


def get_org_service(db: AsyncSession = Depends(get_db)) -> OrganizationService:
    return OrganizationService(db)


@router.get("/organizations", response_model=PaginatedResponse[OrganizationRead])
async def list_organizations(
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    service: OrganizationService = Depends(get_org_service),
) -> PaginatedResponse[OrganizationRead]:
    items, total = await service.list_organizations(limit=limit, offset=offset)
    return PaginatedResponse(items=items, total=total, limit=limit, offset=offset)


@router.post(
    "/organizations",
    response_model=OrganizationRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_organization(
    payload: OrganizationCreate,
    service: OrganizationService = Depends(get_org_service),
) -> OrganizationRead:
    return await service.create_organization(payload)


@router.get("/organizations/{organization_id}", response_model=OrganizationRead)
async def get_organization(
    organization_id: UUID,
    service: OrganizationService = Depends(get_org_service),
) -> OrganizationRead:
    return await service.get_organization(organization_id)


@router.get(
    "/organizations/{organization_id}/departments",
    response_model=list[DepartmentRead],
)
async def list_departments(
    organization_id: UUID,
    service: OrganizationService = Depends(get_org_service),
) -> list[DepartmentRead]:
    return await service.list_departments(organization_id)


@router.post(
    "/departments",
    response_model=DepartmentRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_department(
    payload: DepartmentCreate,
    service: OrganizationService = Depends(get_org_service),
) -> DepartmentRead:
    return await service.create_department(payload)


@router.get("/departments/{department_id}/teams", response_model=list[TeamRead])
async def list_teams(
    department_id: UUID,
    service: OrganizationService = Depends(get_org_service),
) -> list[TeamRead]:
    return await service.list_teams(department_id)


@router.post("/teams", response_model=TeamRead, status_code=status.HTTP_201_CREATED)
async def create_team(
    payload: TeamCreate,
    service: OrganizationService = Depends(get_org_service),
) -> TeamRead:
    return await service.create_team(payload)


@router.get("/teams/{team_id}/employees", response_model=list[EmployeeRead])
async def list_employees(
    team_id: UUID,
    service: OrganizationService = Depends(get_org_service),
) -> list[EmployeeRead]:
    return await service.list_employees(team_id)


@router.post(
    "/employees",
    response_model=EmployeeRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_employee(
    payload: EmployeeCreate,
    service: OrganizationService = Depends(get_org_service),
) -> EmployeeRead:
    return await service.create_employee(payload)
