"use client";

import {
  AlertCircle,
  CheckCircle2,
  Database,
  HardDrive,
  RefreshCw,
  Server,
  Zap,
} from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { useReadinessHealth } from "@/hooks/use-health";

export default function OverviewPage() {
  const { data, isLoading, isError, error, refetch, isFetching } =
    useReadinessHealth();

  const dependencies = [
    {
      key: "postgres",
      name: "PostgreSQL + pgvector",
      icon: Database,
      health: data?.dependencies.postgres,
      detail: data?.dependencies.postgres.pgvector_enabled
        ? "pgvector extension enabled"
        : "pgvector check pending",
    },
    {
      key: "redis",
      name: "Redis (Cache & ARQ)",
      icon: Zap,
      health: data?.dependencies.redis,
      detail: "Task queue and durable session state",
    },
    {
      key: "minio",
      name: "MinIO Object Storage",
      icon: HardDrive,
      health: data?.dependencies.minio,
      detail: data?.dependencies.minio.bucket
        ? `Bucket: ${data.dependencies.minio.bucket}`
        : "Artifact storage",
    },
  ];

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">
            Platform Overview
          </h1>
          <p className="text-sm text-muted-foreground mt-1">
            Phase 0 Foundation — Live infrastructure health and service readiness
          </p>
        </div>

        <Button
          variant="outline"
          size="sm"
          onClick={() => refetch()}
          disabled={isFetching}
        >
          <RefreshCw
            className={`mr-2 h-4 w-4 ${isFetching ? "animate-spin" : ""}`}
          />
          Refresh Health
        </Button>
      </div>

      {isError && (
        <Card className="border-destructive/50 bg-destructive/5">
          <CardHeader>
            <div className="flex items-center gap-2 text-destructive">
              <AlertCircle className="h-5 w-5" />
              <CardTitle>Backend API Unreachable</CardTitle>
            </div>
            <CardDescription>
              {error instanceof Error
                ? error.message
                : "Unable to connect to the FastAPI backend."}
            </CardDescription>
          </CardHeader>
        </Card>
      )}

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Backend API</CardTitle>
            <Server className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            {isLoading ? (
              <div className="text-sm text-muted-foreground">Checking...</div>
            ) : data ? (
              <div className="space-y-1">
                <div className="flex items-center gap-2">
                  <CheckCircle2 className="h-4 w-4 text-emerald-500" />
                  <span className="text-lg font-semibold capitalize">
                    {data.status}
                  </span>
                </div>
                <p className="text-xs text-muted-foreground">
                  v{data.version} · {data.environment}
                </p>
              </div>
            ) : (
              <Badge variant="destructive">Offline</Badge>
            )}
          </CardContent>
        </Card>

        {dependencies.map((dep) => {
          const Icon = dep.icon;
          const isHealthy = dep.health?.status === "healthy";
          return (
            <Card key={dep.key}>
              <CardHeader className="flex flex-row items-center justify-between pb-2">
                <CardTitle className="text-sm font-medium">{dep.name}</CardTitle>
                <Icon className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                {isLoading ? (
                  <div className="text-sm text-muted-foreground">Checking...</div>
                ) : dep.health ? (
                  <div className="space-y-1">
                    <div className="flex items-center justify-between">
                      <Badge variant={isHealthy ? "success" : "destructive"}>
                        {dep.health.status}
                      </Badge>
                      <span className="text-xs text-muted-foreground">
                        {dep.health.latency_ms} ms
                      </span>
                    </div>
                    <p className="text-xs text-muted-foreground truncate">
                      {dep.health.error ?? dep.detail}
                    </p>
                  </div>
                ) : (
                  <Badge variant="secondary">Unknown</Badge>
                )}
              </CardContent>
            </Card>
          );
        })}
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Architecture &amp; Phase Roadmap</CardTitle>
          <CardDescription>
            Modular monolith foundation verified before building Phase 1+ domain modules.
          </CardDescription>
        </CardHeader>
        <CardContent className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3 text-sm">
          <div className="rounded-md border p-3">
            <div className="font-medium">Phase 0: Foundation</div>
            <p className="text-xs text-muted-foreground mt-1">
              FastAPI, Next.js App Router, PostgreSQL + pgvector, Redis + ARQ, MinIO, Docker Compose, health checks.
            </p>
          </div>
          <div className="rounded-md border p-3">
            <div className="font-medium">Phase 1: Organization</div>
            <p className="text-xs text-muted-foreground mt-1">
              Auth, Organizations, 12 Engineering Departments, Teams, AI Employee profiles &amp; hierarchy.
            </p>
          </div>
          <div className="rounded-md border p-3">
            <div className="font-medium">Phase 2–6: Runtime &amp; Delivery</div>
            <p className="text-xs text-muted-foreground mt-1">
              LLM Providers, Tool Registry, Multi-Agent Orchestration, Projects, Workflows, Code Workspace, Analytics.
            </p>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
