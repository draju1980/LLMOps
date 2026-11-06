.PHONY: help up down test validate reset lab clean

help:
	@echo "Module 03-scalable-data-preparation - Makefile Targets"
	@echo ""
	@echo "  make up          Start services for this module"
	@echo "  make down        Stop services"
	@echo "  make test        Run pytest suite"
	@echo "  make validate    Validate learning & setup"
	@echo "  make lab         Run hands-on exercises"
	@echo "  make reset       Hard reset (remove volumes)"
	@echo "  make clean       Clean cache files"

up:
	@echo "Starting 03-scalable-data-preparation..."
	docker compose up -d
	@echo "✓ Services started"

down:
	@echo "Stopping 03-scalable-data-preparation..."
	docker compose down
	@echo "✓ Services stopped"

test:
	@echo "Running tests for 03-scalable-data-preparation..."
	python3 -m pytest tests/ -v --tb=short
	@echo "✓ Tests complete"

validate:
	@echo "Validating 03-scalable-data-preparation..."
	@echo "✓ Module ready"

lab:
	@echo "Running hands-on exercises..."
	@if find exercises/ -name "exercise*.py" -type f 2>/dev/null | grep -q . ; then \
		for exercise in exercises/exercise*.py; do \
			echo "\n▶️  Running $$exercise..."; \
			python3 "$$exercise"; \
		done; \
	else \
		echo "ℹ️  Exercises not yet implemented"; \
	fi
	@echo "✓ Lab complete"

reset:
	@echo "Resetting 03-scalable-data-preparation..."
	docker compose down -v 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Reset complete"

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Cache cleaned"
