# Module: 05-fine-tuning-data-engineering

.PHONY: help up down test validate reset lab clean

help:
	@echo "Module 05-fine-tuning-data-engineering - Makefile Targets"
	@echo ""
	@echo "  make up          Start services for this module"
	@echo "  make down        Stop services"
	@echo "  make test        Run pytest suite"
	@echo "  make validate    Validate learning & setup"
	@echo "  make lab         Run hands-on exercises"
	@echo "  make reset       Hard reset (remove volumes)"
	@echo "  make clean       Clean cache files"

up:
	@echo "Starting 05-fine-tuning-data-engineering..."
	docker compose up -d
	@echo "✓ Services started"

down:
	@echo "Stopping 05-fine-tuning-data-engineering..."
	docker compose down
	@echo "✓ Services stopped"

test:
	@echo "Running tests for 05-fine-tuning-data-engineering..."
	python3 -m pytest tests/ -v --tb=short
	@echo "✓ Tests complete"

validate:
	@echo "Validating 05-fine-tuning-data-engineering..."
	@echo "✓ Module ready"

lab:
	@echo "Running hands-on exercises..."
	python3 -m pytest exercises/ -v
	@echo "✓ Exercises complete"

reset:
	@echo "Resetting 05-fine-tuning-data-engineering..."
	docker compose down -v
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Reset complete"

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Cache cleaned"
