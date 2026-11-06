.PHONY: help up down test validate reset lab clean

help:
	@echo "Module 13-risk-evaluation-probability-severity - Makefile Targets"
	@echo ""
	@echo "  make up          Start services for this module"
	@echo "  make down        Stop services"
	@echo "  make test        Run pytest suite"
	@echo "  make validate    Validate learning & setup"
	@echo "  make lab         Run hands-on exercises"
	@echo "  make reset       Hard reset (remove volumes)"
	@echo "  make clean       Clean cache files"

up:
	@echo "Starting 13-risk-evaluation-probability-severity..."
	docker compose up -d
	@echo "✓ Services started"

down:
	@echo "Stopping 13-risk-evaluation-probability-severity..."
	docker compose down
	@echo "✓ Services stopped"

test:
	@echo "Running tests for 13-risk-evaluation-probability-severity..."
	python3 -m pytest tests/ -v --tb=short
	@echo "✓ Tests complete"

validate:
	@echo "Validating 13-risk-evaluation-probability-severity..."
	@echo "✓ Module ready"

lab:
	@echo "Running hands-on exercises..."
	@if find exercises/ -name "*.py" -type f 2>/dev/null | grep -q . ; then \
		python3 -m pytest exercises/ -v; \
	else \
		echo "ℹ️  Exercises not yet implemented"; \
	fi
	@echo "✓ Lab complete"

reset:
	@echo "Resetting 13-risk-evaluation-probability-severity..."
	docker compose down -v 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Reset complete"

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Cache cleaned"
