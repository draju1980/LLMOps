#!/bin/bash

# Infrastructure validation script
# Checks health of all shared services

set -e

echo "=== LLMOps Infrastructure Validation ==="

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Track failures
FAILURES=0

check_service() {
    local name=$1
    local host=$2
    local port=$3
    local check_cmd=$4

    echo -n "Checking ${name}... "

    if eval "$check_cmd" > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC}"
    else
        echo -e "${RED}✗${NC}"
        FAILURES=$((FAILURES + 1))
    fi
}

# PostgreSQL
check_service "PostgreSQL" "postgres" "5432" \
    "docker exec llmops-postgres pg_isready -U llmops"

# MinIO (LocalStack S3)
check_service "MinIO (S3)" "minio" "4566" \
    "curl -s http://localhost:4566/health | grep -q running"

# Redis
check_service "Redis" "redis" "6379" \
    "docker exec llmops-redis redis-cli ping | grep -q PONG"

# Prometheus
check_service "Prometheus" "prometheus" "9090" \
    "curl -s http://localhost:9090/-/healthy"

# Grafana
check_service "Grafana" "grafana" "3000" \
    "curl -s http://localhost:3000/api/health"

# Jaeger
check_service "Jaeger" "jaeger" "16686" \
    "curl -s http://localhost:16686/"

# MLflow
check_service "MLflow" "mlflow" "5000" \
    "curl -s http://localhost:5000/"

# Qdrant
check_service "Qdrant" "qdrant" "6333" \
    "curl -s http://localhost:6333/health"

echo ""
echo "=== Summary ==="

if [ $FAILURES -eq 0 ]; then
    echo -e "${GREEN}All services healthy! ✓${NC}"
    echo ""
    echo "Access points:"
    echo "  Prometheus:  http://localhost:9090"
    echo "  Grafana:     http://localhost:3000 (admin/admin)"
    echo "  Jaeger UI:   http://localhost:16686"
    echo "  MLflow:      http://localhost:5000"
    echo "  LocalStack:  http://localhost:4566 (S3 endpoint)"
    echo "  Qdrant:      http://localhost:6333"
    echo ""
    exit 0
else
    echo -e "${RED}${FAILURES} service(s) failed health check${NC}"
    exit 1
fi
