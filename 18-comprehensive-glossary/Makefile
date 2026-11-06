.PHONY: help up down test validate reset lab clean

help:
	@echo "Module 18: Comprehensive Glossary - Makefile Targets"
	@echo ""
	@echo "  make up          Start services (conceptual module)"
	@echo "  make down        Stop services"
	@echo "  make test        Run pytest suite"
	@echo "  make validate    Validate learning"
	@echo "  make lab         Run exercises"
	@echo "  make reset       Hard reset"
	@echo "  make clean       Clean cache files"

up:
	@echo "Module 18 is conceptual - no Docker services required"
	@echo "✓ Educational environment ready"

down:
	@echo "Module 18 environment stopped"

test:
	@echo "Running Module 18 tests..."
	python3 -m pytest tests/ -v --tb=short

validate:
	@echo "Validating Module 18 learning..."
	@echo "✓ Module 18 ready"

lab:
	@echo "Module 18: Glossary Review"
	@echo "See src/ directory for glossary content"

reset:
	rm -rf __pycache__ .pytest_cache *.pyc
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Module 18 reset complete"

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Cache cleaned"
