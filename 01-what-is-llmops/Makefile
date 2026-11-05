.PHONY: help up down test validate reset lab clean

help:
	@echo "Module 01: What is LLMOps? - Makefile Targets"
	@echo ""
	@echo "  make up          Start services (minimal; mostly educational)"
	@echo "  make down        Stop services"
	@echo "  make test        Run Python tests and exercises"
	@echo "  make validate    Validate understanding (interactive quiz)"
	@echo "  make lab         Run hands-on exercises"
	@echo "  make reset       Hard reset (remove volumes)"
	@echo "  make clean       Clean __pycache__ and .pyc files"
	@echo ""
	@echo "Quick Start:"
	@echo "  make up && make lab"

up:
	@echo "Module 01 is mostly conceptual - no Docker services required"
	@echo "✓ Educational environment ready"

down:
	@echo "Module 01 environment stopped"

test:
	@echo "Running Module 01 tests..."
	python -m pytest tests/ -v --tb=short

validate:
	@echo "Validating Module 01 learning..."
	python src/01_paradigm_shift.py
	python src/02_nine_pillars.py
	@echo ""
	@echo "✓ Module 01 concepts validated"

lab:
	@echo "Module 01: Hands-On Exercises"
	@echo ""
	@echo "Exercise 1.1: Paradigm Shift Identification"
	python exercises/exercise_1_1.py
	@echo ""
	@echo "Exercise 1.2: 9 Pillars Mapping"
	python exercises/exercise_1_2.py
	@echo ""
	@echo "See solutions/ directory for detailed answers"

reset:
	rm -rf __pycache__ .pytest_cache *.pyc
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Module 01 reset complete"

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Cache cleaned"
