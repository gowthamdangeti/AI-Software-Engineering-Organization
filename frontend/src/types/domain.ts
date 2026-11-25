export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  limit: number;
  offset: number;
}

export interface Organization {
  id: string;
  name: string;
  slug: string;
  description: string | null;
  settings: Record<string, unknown>;
  created_at: string;
  updated_at: string;
}

export interface Department {
  id: string;
  organization_id: string;
  name: string;
  description: string | null;
  head_employee_id: string | null;
  created_at: string;
  updated_at: string;
}

export interface Team {
  id: string;
  department_id: string;
  name: string;
  mission: string | null;
  lead_employee_id: string | null;
  created_at: string;
  updated_at: string;
}

export interface Employee {
  id: string;
  team_id: string;
  manager_id: string | null;
  name: string;
  role: string;
  seniority: string;
  status: string;
  model_provider: string;
  model_name: string;
  system_prompt: string | null;
  capabilities: string[];
  created_at: string;
  updated_at: string;
}

export interface Project {
  id: string;
  organization_id: string;
  name: string;
  description: string | null;
  repository_url: string | null;
  status: string;
  created_at: string;
  updated_at: string;
}

export interface Task {
  id: string;
  project_id: string;
  assignee_id: string | null;
  parent_task_id: string | null;
  title: string;
  description: string | null;
  status: string;
  priority: number;
  extra_metadata: Record<string, unknown>;
  created_at: string;
  updated_at: string;
}

export interface Workflow {
  id: string;
  project_id: string;
  name: string;
  description: string | null;
  status: string;
  definition: Record<string, unknown>;
  created_at: string;
  updated_at: string;
}
