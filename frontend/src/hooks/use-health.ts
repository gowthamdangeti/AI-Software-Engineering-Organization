"use client";

import { useQuery } from "@tanstack/react-query";
import { fetchReadinessHealth } from "@/services/health";

export function useReadinessHealth() {
  return useQuery({
    queryKey: ["system", "health", "ready"],
    queryFn: fetchReadinessHealth,
    refetchInterval: 15_000,
    retry: 1,
  });
}
