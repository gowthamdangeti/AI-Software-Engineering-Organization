export interface DependencyHealth {
  status: "healthy" | "unhealthy";
  latency_ms: number;
  pgvector_enabled?: boolean;
  bucket?: string;
  bucket_exists?: boolean;
  error?: string;
}

export interface ReadinessResponse {
  status: "ready" | "degraded";
  service: string;
  version: string;
  environment: string;
  timestamp: string;
  dependencies: {
    postgres: DependencyHealth;
    redis: DependencyHealth;
    minio: DependencyHealth;
  };
}
