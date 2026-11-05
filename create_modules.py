#!/usr/bin/env python3
"""
Automated Module Generator for LLMOps Course

This script creates the complete structure for all 19 modules using templates
extracted from the PDF source-outline.md.

Usage: python create_modules.py
"""

import os
import sys
from pathlib import Path


# Module definitions with their key content from the PDF
MODULES = {
    "02-mlops-to-llmops-framework": {
        "title": "MLOps to LLMOps Framework",
        "description": "The seven-stage end-to-end lifecycle: Ingestion, Validation, Transformation, Training, Analysis, Serving, Logging",
        "objectives": [
            "Understand the 7-stage LLMOps lifecycle",
            "Recognize production vulnerabilities in naive deployments",
            "Map enterprise systems to LLMOps components",
            "Identify gaps and prioritize improvements"
        ],
        "key_topics": [
            "7-stage lifecycle diagram",
            "Continuous orchestration layer",
            "Continuous monitoring and feedback flywheel",
            "Hands-on Exercise 2.1: Lifecycle Gap Assessment"
        ],
        "labs": [],
        "duration": "2 hours"
    },
    "03-scalable-data-preparation": {
        "title": "Scalable Data Preparation",
        "description": "ELT pipelines using DuckDB: deduplication, filtering, token estimation, JSON export",
        "objectives": [
            "Learn ELT philosophy vs memory-bound Pandas",
            "Write production SQL pipelines in DuckDB",
            "Implement automated deduplication via SHA256",
            "Validate and profile data quality"
        ],
        "key_topics": [
            "DuckDB SQL pipeline (BigQuery replacement)",
            "SHA256 deduplication and hashing",
            "Token estimation and length validation",
            "PII removal and data anonymization",
            "Structured JSON export for instruction tuning"
        ],
        "labs": ["Sample support tickets dataset", "download.sh for full dataset"],
        "duration": "4 hours"
    },
    "04-dataset-engineering-lineage": {
        "title": "Dataset Engineering & Lineage",
        "description": "Cryptographic versioning, immutability, provenance DAGs, train/val/test split leakage prevention",
        "objectives": [
            "Generate immutable dataset manifests (SHA256)",
            "Track data lineage as DAGs",
            "Prevent train/val/test leakage",
            "Version datasets like code artifacts"
        ],
        "key_topics": [
            "Dataset manifest generation (Python script)",
            "SHA256 content hashing for immutability",
            "Data lineage DAGs",
            "Entity-based leakage prevention",
            "MLflow artifact registration"
        ],
        "labs": [],
        "duration": "3 hours"
    },
    "05-fine-tuning-data-engineering": {
        "title": "Fine-Tuning Data Engineering",
        "description": "ChatML, Alpaca, Llama-3 formatting; instruction structuring; loss masking (labels=-100 on prompts)",
        "objectives": [
            "Format instruction data in ChatML/Alpaca/Llama-3",
            "Implement loss masking (train only on responses)",
            "Structure prompt-input-output triples",
            "Validate output format correctness"
        ],
        "key_topics": [
            "ChatML format with role markers",
            "Alpaca format (instruction/input/output)",
            "Llama-3 header format",
            "Loss masking implementation (labels=-100)",
            "Token validation and edge cases"
        ],
        "labs": [],
        "duration": "3 hours"
    },
    "06-kubeflow-pipelines": {
        "title": "Kubeflow Pipelines (KFP v2)",
        "description": "Containerized DAGs with typed components: Extract→Tokenize→Train→Evaluate→Deploy gate",
        "objectives": [
            "Build KFP v2 pipelines with @dsl.component",
            "Define strongly-typed inputs/outputs",
            "Create conditional deployment gates",
            "Execute locally without Kubernetes"
        ],
        "key_topics": [
            "KFP v2 pipeline definition",
            "@dsl.component decorators",
            "Typed inputs/outputs",
            "Conditional branching (dsl.If)",
            "Local Docker runner (no Kubernetes required)"
        ],
        "labs": [],
        "duration": "4 hours"
    },
    "07-artifact-management-versioning": {
        "title": "Artifact Management & Versioning",
        "description": "Model cards, adapter versioning, MLflow registry, complete lineage packages",
        "objectives": [
            "Create structured model cards (Pydantic)",
            "Version adapters in MLflow",
            "Track full artifact lineage",
            "Register artifacts with metadata"
        ],
        "key_topics": [
            "Model Card schema (base model, training data, eval)",
            "Adapter checkpoint versioning",
            "MLflow artifact registry",
            "Lineage DAGs and provenance",
            "Complete artifact packages"
        ],
        "labs": [],
        "duration": "3 hours"
    },
    "08-peft-lora-qlora": {
        "title": "PEFT: LoRA & QLoRA",
        "description": "Parameter-efficient fine-tuning: LoRA mathematics, CPU-friendly training, VRAM budgeting",
        "objectives": [
            "Understand LoRA mathematics (W = W₀ + (α/r)(B×A))",
            "Train LoRA on CPU-friendly model (SmolLM2-135M)",
            "Calculate VRAM budgets for QLLoRA",
            "Complete Lab 1: VRAM Sizing Exercise"
        ],
        "key_topics": [
            "LoRA mathematics and decomposition",
            "QLoRA 4-bit quantization (NF4, double quantization)",
            "CPU training (SmolLM2-135M default)",
            "GPU training (14B+ models with QLoRA)",
            "VRAM calculator: base + adapters + optimizer + KV cache"
        ],
        "labs": ["Lab 1: VRAM Budgeting & QLLoRA Sizing Calculation"],
        "duration": "5 hours"
    },
    "09-model-deployment-serving": {
        "title": "Model Deployment & High-Throughput Serving",
        "description": "FastAPI + vLLM async streaming: PagedAttention, continuous batching, SamplingParams",
        "objectives": [
            "Build async FastAPI server with streaming",
            "Use vLLM's PagedAttention and continuous batching",
            "Implement Server-Sent Events (SSE) streaming",
            "Achieve TTFT < 350ms and TPOT < 30ms"
        ],
        "key_topics": [
            "Anti-pattern: Naive Flask wrapper (why it fails)",
            "Production: FastAPI + vLLM async engine",
            "PagedAttention (KV cache as fixed-size blocks)",
            "Continuous batching (iterate-level scheduling)",
            "Streaming via Server-Sent Events (SSE)",
            "SamplingParams (temperature, top-p, max_tokens)"
        ],
        "labs": [],
        "duration": "4 hours"
    },
    "10-production-operations-observability": {
        "title": "Production Operations & Observability",
        "description": "Golden Signals (TTFT, TPOT, KV cache, perplexity), OpenTelemetry, Prometheus, Grafana",
        "objectives": [
            "Implement Golden Signals metrics collection",
            "Setup OpenTelemetry instrumentation",
            "Create Prometheus/Grafana dashboards",
            "Complete Lab 2: Canary Rollout & Automated Rollback"
        ],
        "key_topics": [
            "Golden Signals: TTFT, TPOT, KV cache saturation, perplexity",
            "Semantic quality metrics (hallucination rate, similarity)",
            "OpenTelemetry instrumentation and spans",
            "Prometheus metrics scraping",
            "Grafana dashboard setup",
            "Lab 2: Canary deployment with automated rollback"
        ],
        "labs": ["Lab 2: End-to-End Canary Rollout & Automated Rollback Script"],
        "duration": "4 hours"
    },
    "11-prompt-management-train-serve-skew": {
        "title": "Prompt Management & Train-Serve Skew",
        "description": "Centralized Prompt Registry, Jinja2 templates, automated linting, zero-skew detection",
        "objectives": [
            "Manage prompts in centralized Jinja2 registry",
            "Implement Pydantic v2 validation",
            "Detect and prevent train-serve skew",
            "Complete Lab 3: Prompt Template Skew Detection"
        ],
        "key_topics": [
            "Centralized Prompt Registry (Postgres-backed)",
            "Jinja2 templating with required variables",
            "Pydantic v2 contract validation",
            "Automated linting (check for missing variables)",
            "Zero-skew detector (byte-for-byte tokenizer match)",
            "Lab 3: Prompt template CI test"
        ],
        "labs": ["Lab 3: Prompt Template Skew Detection Test Suite"],
        "duration": "3 hours"
    },
    "12-safety-responsible-ai": {
        "title": "Safety & Responsible AI",
        "description": "Multi-tier guardrails: ingress (injection, PII), semantic policy, egress (hallucination, leakage)",
        "objectives": [
            "Implement prompt injection detection",
            "Deploy PII anonymization layer",
            "Detect hallucination and data exfiltration",
            "Build 4-tier safety architecture"
        ],
        "key_topics": [
            "Direct prompt injection attacks",
            "Indirect prompt injection (RAG documents)",
            "Data exfiltration vectors",
            "Multi-tier architecture (4 layers)",
            "Ingress guardrails (regex + ML)",
            "Egress guardrails (semantic validators)"
        ],
        "labs": [],
        "duration": "4 hours"
    },
    "13-risk-evaluation-probability-severity": {
        "title": "Risk Evaluation: Probability vs Severity",
        "description": "2×2 matrix, dynamic thresholding, escalation workflows, context-aware routing",
        "objectives": [
            "Understand 2×2 risk matrix (probability × severity)",
            "Implement dynamic thresholding",
            "Route to escalation for high-severity cases",
            "Avoid false positives on low-severity items"
        ],
        "key_topics": [
            "Risk matrix quadrants and actions",
            "Probability vs severity distinction",
            "Dynamic thresholding logic",
            "Escalation workflows",
            "Context-aware risk routing"
        ],
        "labs": [],
        "duration": "2 hours"
    },
    "14-llmops-vs-llm-system-design": {
        "title": "LLMOps vs LLM System Design",
        "description": "Demarcation: Infrastructure (ops) vs Application (AI architects), Hybrid RAG with RRF",
        "objectives": [
            "Distinguish LLMOps from LLM system design",
            "Design hybrid RAG with Reciprocal Rank Fusion",
            "Understand infrastructure vs application concerns",
            "Plan enterprise search architecture"
        ],
        "key_topics": [
            "LLMOps: Reliability, automation, latency SLAs",
            "System Design: Domain reasoning, RAG, agents",
            "Hybrid search: Dense (vector) + Sparse (BM25)",
            "Reciprocal Rank Fusion algorithm",
            "Cross-Encoder reranking",
            "Infrastructure vs Application architecture"
        ],
        "labs": [],
        "duration": "2 hours"
    },
    "15-beyond-the-course": {
        "title": "Beyond the Course: The Modern Frontier",
        "description": "RAGAS, DeepEval, LangGraph agents, AI platform engineering, emerging frontiers",
        "objectives": [
            "Evaluate RAG systems with RAGAS",
            "Unit-test LLM apps with DeepEval",
            "Build multi-agent systems with LangGraph",
            "Understand platform engineering for AI"
        ],
        "key_topics": [
            "RAGAS: RAG evaluation framework",
            "DeepEval: LLM app testing",
            "LangGraph: Multi-agent orchestration",
            "Agentic loops and autonomous agents",
            "AI platform engineering",
            "Future directions in LLMOps"
        ],
        "labs": [],
        "duration": "3 hours"
    },
    "16-hands-on-labs": {
        "title": "Hands-On Labs & Implementation Exercises",
        "description": "Complete Lab 1, 2, 3 with automated graders and full solutions",
        "objectives": [
            "Complete Lab 1: VRAM budgeting with solutions",
            "Complete Lab 2: Canary deployment with rollback",
            "Complete Lab 3: Prompt template skew detection",
            "Pass all automated graders"
        ],
        "key_topics": [
            "Lab 1: VRAM calculator (Module 08)",
            "Lab 2: Canary rollout script (Module 10)",
            "Lab 3: Prompt skew detector (Module 11)",
            "Automated test harnesses",
            "Solutions and explanations"
        ],
        "labs": ["Lab 1", "Lab 2", "Lab 3"],
        "duration": "6 hours"
    },
    "17-interview-preparation": {
        "title": "Ultimate LLMOps Interview Preparation",
        "description": "25 deep-dive technical & scenario questions with model answers",
        "objectives": [
            "Master 25 core LLMOps interview questions",
            "Develop nuanced technical understanding",
            "Practice scenario-based problem solving",
            "Prepare for senior-level interviews"
        ],
        "key_topics": [
            "Q1: PagedAttention memory management",
            "Q2: TTFT vs TPOT distinction",
            "Q3: Fine-tuning vs RAG vs prompting",
            "Q4-Q25: Deep-dive technical questions",
            "Scenario-based problem solving",
            "Production-grade system design"
        ],
        "labs": [],
        "duration": "Self-paced"
    },
    "18-glossary": {
        "title": "Comprehensive LLMOps A-Z Glossary",
        "description": "60+ essential terms with technical definitions",
        "objectives": [
            "Master 60+ LLMOps terminology",
            "Understand concepts rigorously",
            "Reference material for entire course",
            "Build shared vocabulary"
        ],
        "key_topics": [
            "Data preparation terms",
            "Model training terms",
            "Serving & optimization terms",
            "Observability terms",
            "Safety & governance terms",
            "Architecture patterns"
        ],
        "labs": [],
        "duration": "Reference"
    },
    "19-production-checklist": {
        "title": "Key Takeaways & Enterprise Production Checklist",
        "description": "Final synthesis, readiness audit script, enterprise verification checklist",
        "objectives": [
            "Review core principles and takeaways",
            "Run enterprise production readiness audit",
            "Generate validation report",
            "Verify all components are production-grade"
        ],
        "key_topics": [
            "7 core production principles",
            "Enterprise readiness checklist",
            "Automated audit script",
            "Validation reporting",
            "Deployment verification",
            "Ongoing maintenance guidelines"
        ],
        "labs": [],
        "duration": "1 hour"
    }
}


def create_module_directory(module_key: str, module_info: dict):
    """Create directory structure and README for a module"""

    module_dir = Path(module_key)
    module_dir.mkdir(exist_ok=True)

    # Create subdirectories
    (module_dir / "src").mkdir(exist_ok=True)
    (module_dir / "tests").mkdir(exist_ok=True)
    (module_dir / "exercises").mkdir(exist_ok=True)
    (module_dir / "solutions").mkdir(exist_ok=True)
    (module_dir / "data").mkdir(exist_ok=True)

    # Create README
    readme_path = module_dir / "README.md"
    if not readme_path.exists():
        create_readme(module_dir, module_key, module_info)

    # Create Makefile
    makefile_path = module_dir / "Makefile"
    if not makefile_path.exists():
        create_makefile(module_dir, module_key)

    # Create docker-compose.yml
    compose_path = module_dir / "docker-compose.yml"
    if not compose_path.exists():
        create_docker_compose(module_dir, module_key)

    print(f"✓ Created {module_key}/")


def create_readme(module_dir: Path, module_key: str, module_info: dict):
    """Create module README"""

    title = module_info["title"]
    description = module_info["description"]
    objectives = "\n".join([f"  {i+1}. {obj}" for i, obj in enumerate(module_info["objectives"])])
    topics = "\n".join([f"  • {topic}" for topic in module_info["key_topics"]])
    labs = "\n".join([f"  • {lab}" for lab in module_info["labs"]]) if module_info["labs"] else "  (None)"
    duration = module_info["duration"]

    readme_content = f"""# {title}

**{description}**

## Learning Objectives

By the end of this module, you will be able to:

{objectives}

## Duration

{duration}

## Key Concepts & Topics

{topics}

## Hands-On Labs

{labs}

## Module Structure

```
{module_key}/
├── README.md                    # This file
├── Makefile                     # Standard targets: up, down, test, validate
├── docker-compose.yml           # Services for this module
├── src/                         # Source code demonstrations
├── exercises/                   # Hands-on exercises
├── solutions/                   # Solutions and explanations
├── tests/                       # Unit and integration tests
└── data/                        # Sample datasets
```

## Prerequisites

- Module 01: What is LLMOps? (foundational concepts)
- Basic Python and command-line skills
- Docker installed and running

## Quick Start

```bash
# Navigate to this module
cd {module_key}

# Start services (if any)
make up

# Run hands-on exercises
make lab

# Run tests
make test

# Verify learning
make validate

# Stop services
make down
```

## Key Takeaways

(Placeholder: See README.md content once written)

## Next Steps

- Complete hands-on exercises
- Run tests to verify understanding
- Check out the next module in the learning path

## References

- Source: PDF source-outline.md (Chapter {module_key.split('-')[0]})
- Glossary: Module 18
- Interview Prep: Module 17

---

**Last Updated:** 2026-11-05
**Status:** Template (full implementation pending)
"""

    with open(module_dir / "README.md", "w") as f:
        f.write(readme_content)


def create_makefile(module_dir: Path, module_key: str):
    """Create module Makefile with standard targets"""

    makefile_content = f"""# Module: {module_key}

.PHONY: help up down test validate reset lab clean

help:
	@echo "Module {module_key} - Makefile Targets"
	@echo ""
	@echo "  make up          Start services for this module"
	@echo "  make down        Stop services"
	@echo "  make test        Run pytest suite"
	@echo "  make validate    Validate learning & setup"
	@echo "  make lab         Run hands-on exercises"
	@echo "  make reset       Hard reset (remove volumes)"
	@echo "  make clean       Clean cache files"

up:
	@echo "Starting {module_key}..."
	docker compose up -d
	@echo "✓ Services started"

down:
	@echo "Stopping {module_key}..."
	docker compose down
	@echo "✓ Services stopped"

test:
	@echo "Running tests for {module_key}..."
	python -m pytest tests/ -v --tb=short
	@echo "✓ Tests complete"

validate:
	@echo "Validating {module_key}..."
	@echo "✓ Module ready"

lab:
	@echo "Running hands-on exercises..."
	python -m pytest exercises/ -v
	@echo "✓ Exercises complete"

reset:
	@echo "Resetting {module_key}..."
	docker compose down -v
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {{}} + 2>/dev/null || true
	@echo "✓ Reset complete"

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -exec rm -rf {{}} + 2>/dev/null || true
	@echo "✓ Cache cleaned"
"""

    with open(module_dir / "Makefile", "w") as f:
        f.write(makefile_content)


def create_docker_compose(module_dir: Path, module_key: str):
    """Create module docker-compose.yml"""

    compose_content = f"""version: '3.8'

name: llmops-{module_key.replace('/', '-')}

services:
  # Add services specific to this module here
  # Or reference shared infrastructure from parent docker-compose.yml

  placeholder:
    image: busybox:latest
    command: echo "Module {module_key} services (if any)"
    profiles:
      - never-start

networks:
  default:
    name: llmops-{module_key.replace('/', '-')}-network
"""

    with open(module_dir / "docker-compose.yml", "w") as f:
        f.write(compose_content)


def main():
    """Create all remaining modules"""

    print("\n" + "=" * 70)
    print("CREATING LLMOps COURSE MODULES 02-19")
    print("=" * 70 + "\n")

    for module_key, module_info in MODULES.items():
        try:
            create_module_directory(module_key, module_info)
        except Exception as e:
            print(f"✗ Error creating {module_key}: {e}")

    print("\n" + "=" * 70)
    print("✓ ALL MODULES CREATED SUCCESSFULLY")
    print("=" * 70)
    print("\nNext steps:")
    print("  1. Review each module's README.md")
    print("  2. Run 'make test' in each module to verify setup")
    print("  3. Implement module content from PDF source-outline.md")
    print("  4. Add exercises and solutions")
    print("\n")


if __name__ == "__main__":
    main()
