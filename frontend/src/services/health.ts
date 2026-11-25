import { apiFetch } from "@/lib/api-client";
import type { ReadinessResponse } from "@/types/health";

export async function fetchReadinessHealth(): Promise<ReadinessResponse> {
  return apiFetch<ReadinessResponse>("/api/v1/health/ready");
}
