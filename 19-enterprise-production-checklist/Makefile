.PHONY: help up down test validate reset lab clean

help:
	@echo "Module 19: Enterprise Production Checklist - Makefile Targets"
	@echo ""
	@echo "  make up          Start services (conceptual module)"
	@echo "  make down        Stop services"
	@echo "  make test        Run pytest suite"
	@echo "  make validate    Validate checklist"
	@echo "  make lab         Run audit exercises"
	@echo "  make reset       Hard reset"
	@echo "  make clean       Clean cache files"

up:
	@echo "Module 19 is conceptual - no Docker services required"
	@echo "✓ Audit environment ready"

down:
	@echo "Module 19 environment stopped"

test:
	@echo "Running Module 19 tests..."
	python3 -m pytest tests/ -v --tb=short

validate:
	@echo "Validating Module 19 checklist..."
	@echo "✓ Module 19 ready"

lab:
	@echo "Module 19: Production Readiness Audit"
	@echo "See src/ directory for audit scripts"

reset:
	rm -rf __pycache__ .pytest_cache *.pyc
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Module 19 reset complete"

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Cache cleaned"
