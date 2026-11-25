# Phase 0 Architecture Overview

## Overview
The AI-Native Software Engineering Organization is structured as a modular monolith with clear service boundaries:

- **Frontend (`frontend/`)**: Next.js (App Router), TypeScript, Tailwind CSS, Zustand, TanStack Query, React Hook Form, Zod, React Flow, Vitest.
- **Backend (`backend/`)**: FastAPI, Pydantic v2, SQLAlchemy 2.0 (asyncpg), Alembic, Redis, ARQ worker, MinIO SDK, Pytest.
- **Infrastructure (`infrastructure/`, `docker-compose.yml`)**:
  - **PostgreSQL 16 + pgvector**: Primary relational & vector store (`uuid-ossp`, `vector` extensions enabled via `infrastructure/docker/postgres/init.sql`).
  - **Redis 7**: Session/execution state and ARQ background task queue.
  - **MinIO**: S3-compatible local object storage (`ai-org-artifacts` bucket).

## Health Endpoints
- `GET /health` & `GET /api/v1/health`: Liveness probe returning service metadata and timestamp.
- `GET /health/ready` & `GET /api/v1/health/ready`: Readiness probe verifying PostgreSQL (including `pgvector`), Redis (`PING`), and MinIO (bucket existence) with per-dependency latency in milliseconds. Returns HTTP `200` when ready or `503` when any dependency is unhealthy.
