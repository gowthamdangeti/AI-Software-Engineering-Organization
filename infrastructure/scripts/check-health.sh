#!/usr/bin/env bash
set -euo pipefail

API_URL="${NEXT_PUBLIC_API_URL:-http://localhost:8000}"

echo "Checking backend liveness..."
curl -fsS "${API_URL}/health"
echo ""

echo "Checking backend readiness..."
curl -fsS "${API_URL}/api/v1/health/ready"
echo ""
