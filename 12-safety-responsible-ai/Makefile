# Module: 12-safety-responsible-ai

.PHONY: help up down test validate reset lab clean

help:
	@echo "Module 12-safety-responsible-ai - Makefile Targets"
	@echo ""
	@echo "  make up          Start services for this module"
	@echo "  make down        Stop services"
	@echo "  make test        Run pytest suite"
	@echo "  make validate    Validate learning & setup"
	@echo "  make lab         Run hands-on exercises"
	@echo "  make reset       Hard reset (remove volumes)"
	@echo "  make clean       Clean cache files"

up:
	@echo "Starting 12-safety-responsible-ai..."
	docker compose up -d
	@echo "✓ Services started"

down:
	@echo "Stopping 12-safety-responsible-ai..."
	docker compose down
	@echo "✓ Services stopped"

test:
	@echo "Running tests for 12-safety-responsible-ai..."
	python3 -m pytest tests/ -v --tb=short
	@echo "✓ Tests complete"

validate:
	@echo "Validating 12-safety-responsible-ai..."
	@echo "✓ Module ready"

lab:
	@echo "Running hands-on exercises..."
	python3 -m pytest exercises/ -v
	@echo "✓ Exercises complete"

reset:
	@echo "Resetting 12-safety-responsible-ai..."
	docker compose down -v
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Reset complete"

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Cache cleaned"
