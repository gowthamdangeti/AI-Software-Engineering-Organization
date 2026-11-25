import { apiFetch } from "@/lib/api-client";
import type { PaginatedResponse, Project, Task, Workflow } from "@/types/domain";

export const projectService = {
  listProjects: (limit = 50, offset = 0) =>
    apiFetch<PaginatedResponse<Project>>(
      `/api/v1/projects?limit=${limit}&offset=${offset}`
    ),
  getProject: (id: string) => apiFetch<Project>(`/api/v1/projects/${id}`),
  listTasks: (projectId: string) =>
    apiFetch<Task[]>(`/api/v1/projects/${projectId}/tasks`),
  listWorkflows: (projectId: string) =>
    apiFetch<Workflow[]>(`/api/v1/projects/${projectId}/workflows`),
};
