import { apiFetch } from "@/lib/api-client";
import type {
  Department,
  Employee,
  Organization,
  PaginatedResponse,
  Team,
} from "@/types/domain";

export const organizationService = {
  listOrganizations: (limit = 50, offset = 0) =>
    apiFetch<PaginatedResponse<Organization>>(
      `/api/v1/organizations?limit=${limit}&offset=${offset}`
    ),
  getOrganization: (id: string) =>
    apiFetch<Organization>(`/api/v1/organizations/${id}`),
  listDepartments: (organizationId: string) =>
    apiFetch<Department[]>(`/api/v1/organizations/${organizationId}/departments`),
  listTeams: (departmentId: string) =>
    apiFetch<Team[]>(`/api/v1/departments/${departmentId}/teams`),
  listEmployees: (teamId: string) =>
    apiFetch<Employee[]>(`/api/v1/teams/${teamId}/employees`),
};
