from unittest.mock import AsyncMock, patch

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_liveness_root(client: AsyncClient) -> None:
    response = await client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["service"] == "backend"


@pytest.mark.asyncio
async def test_liveness_v1(client: AsyncClient) -> None:
    response = await client.get("/api/v1/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"


@pytest.mark.asyncio
async def test_readiness_all_healthy(client: AsyncClient) -> None:
    with (
        patch(
            "app.api.v1.health.check_database_health",
            new=AsyncMock(return_value={"status": "healthy", "latency_ms": 1.2, "pgvector_enabled": True}),
        ),
        patch(
            "app.api.v1.health.check_redis_health",
            new=AsyncMock(return_value={"status": "healthy", "latency_ms": 0.5}),
        ),
        patch(
            "app.api.v1.health.check_minio_health",
            new=AsyncMock(
                return_value={"status": "healthy", "latency_ms": 2.1, "bucket": "ai-org-artifacts", "bucket_exists": True}
            ),
        ),
    ):
        response = await client.get("/api/v1/health/ready")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ready"
    assert payload["dependencies"]["postgres"]["status"] == "healthy"
    assert payload["dependencies"]["redis"]["status"] == "healthy"
    assert payload["dependencies"]["minio"]["status"] == "healthy"


@pytest.mark.asyncio
async def test_readiness_degraded_returns_503(client: AsyncClient) -> None:
    with (
        patch(
            "app.api.v1.health.check_database_health",
            new=AsyncMock(return_value={"status": "unhealthy", "latency_ms": 5.0, "error": "connection refused"}),
        ),
        patch(
            "app.api.v1.health.check_redis_health",
            new=AsyncMock(return_value={"status": "healthy", "latency_ms": 0.5}),
        ),
        patch(
            "app.api.v1.health.check_minio_health",
            new=AsyncMock(return_value={"status": "healthy", "latency_ms": 1.0, "bucket": "ai-org-artifacts", "bucket_exists": True}),
        ),
    ):
        response = await client.get("/api/v1/health/ready")

    assert response.status_code == 503
    payload = response.json()
    assert payload["status"] == "degraded"
