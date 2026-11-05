# LLMOps Course - Implementation Plan & Build Order

**Status:** Foundation Phase (Infrastructure Setup)

## Overview

This document describes the systematic build order, dependencies, and validation strategy for the LLMOps Complete Course implementation.

### Key Principles

1. **Infrastructure First:** Shared services (Postgres, MinIO, Redis, Prometheus, Grafana) are the foundation
2. **Build Order:** Modules are built in dependency order (not chapter order)
3. **Validation at Each Step:** Each module must pass `make validate` before moving to the next
4. **Reproducibility:** All Docker images, Python packages, and model versions are pinned

---

## Phase 1: Foundation (Weeks 1-2)

### Task 1.1: Shared Infrastructure ✅ (In Progress)

**Components:**
- `docker-compose.yml` with all shared services
- Prometheus configuration + Grafana dashboards
- PostgreSQL initialization (MLflow DB, Prompt Registry schema)
- MinIO bucket setup (datasets, models, artifacts)
- Redis configuration
- Jaeger tracing setup
- Qdrant vector DB initialization

**Validation:**
```bash
make infra-up
make infra-validate    # All 8 services should be healthy
```

**Output:** Infrastructure stack running, all ports accessible

---

## Phase 2: Data Pipeline Modules (Weeks 2-3)

Build order: **03 → 04 → 05 → 07 → 08**

These form the data → training pipeline backbone.

### Task 2.1: Module 03 - Scalable Data Preparation

**Dependencies:** Infrastructure only

**Deliverables:**
- `03-scalable-data-preparation/` with DuckDB ELT pipeline
- SQL script that demonstrates:
  - Raw data ingestion
  - Deduplication (SHA256)
  - Token estimation
  - PII removal
  - Structured JSONL export
- Sample support tickets CSV (few hundred rows)
- `download.sh` script for full dataset (if available)
- Unit tests validating SQL output

**Validation:**
```bash
cd 03-scalable-data-preparation
make up          # Start DuckDB
make test        # Run tests
make validate    # Verify SQL pipeline
```

**Expected Outcomes:**
- `output/cleaned_data.jsonl` with deduplicated examples
- Test coverage for filtering, hashing, deduplication

### Task 2.2: Module 04 - Dataset Engineering & Lineage

**Dependencies:** Module 03

**Deliverables:**
- Dataset manifest generation (SHA256, line count, timestamp, schema version)
- Python script `generate_dataset_manifest()` that creates immutable metadata
- Train/val/test split with entity-based leakage prevention
- MLflow artifact registration
- Example manifests

**Validation:**
```bash
cd 04-dataset-engineering-lineage
make up          # Start Postgres + MLflow
make test        # Verify manifest generation
make validate    # Check artifact versioning
```

### Task 2.3: Module 05 - Fine-Tuning Data Engineering

**Dependencies:** Module 04

**Deliverables:**
- ChatML formatter (structured conversations)
- Alpaca formatter (instruction-input-response)
- Llama-3 header formatter
- Loss masking implementation (labels = -100 on prompt tokens)
- Sample datasets in each format
- Unit test proving loss is only computed on response tokens

**Validation:**
```bash
cd 05-fine-tuning-data-engineering
make test        # Verify loss masking correctness
make validate    # Check all formatters produce valid outputs
```

### Task 2.4: Module 07 - Artifact Management & Versioning

**Dependencies:** Module 04, MLflow infrastructure

**Deliverables:**
- Model Card schema (Pydantic)
- Adapter versioning script
- MLflow integration for artifact registry
- Complete artifact lineage example

**Validation:**
```bash
cd 07-artifact-management-versioning
make up          # Start MLflow
make test        # Verify artifact registration
make validate    # Check model card schema
```

### Task 2.5: Module 08 - PEFT: LoRA & QLoRA

**Dependencies:** Module 07, PyTorch environment

**Deliverables:**
- LoRA mathematics explanation
- CPU-friendly LoRA training on SmolLM2-135M (default)
- QLoRA training on 14B model (GPU profile, optional)
- Lab 1: VRAM calculator with solutions
- Training scripts with configs

**Validation:**
```bash
cd 08-peft-lora-qlora
make up          # Start environment (CPU or GPU profile)
make test        # Quick training test (2 steps, CPU)
make validate    # Run Lab 1 grader
./labs/test_lab_1.py
```

---

## Phase 3: Orchestration & Serving (Weeks 3-4)

Build order: **06 → 09 → 10 → 16**

### Task 3.1: Module 06 - Kubeflow Pipelines

**Dependencies:** Modules 03-05, Postgres

**Deliverables:**
- KFP v2 pipeline with @dsl.component decorators
- 5-step DAG: Extract → Tokenize → Train → Evaluate → [Gate] → Deploy
- Local Docker runner (no Kubernetes required)
- Compiled YAML output
- Integration tests

**Validation:**
```bash
cd 06-kubeflow-pipelines
make up          # Start Postgres + KFP backend
make test        # Compile and run pipeline locally
make validate    # Verify DAG execution
```

### Task 3.2: Module 09 - Model Deployment & Serving

**Dependencies:** Module 08

**Deliverables:**
- Anti-pattern: Naive Flask server (why it fails)
- Production: FastAPI + vLLM async streaming
- SamplingParams configuration
- Streaming response handler
- Integration tests with curl

**Validation:**
```bash
cd 09-model-deployment-serving
make up          # Start vLLM (or Ollama on CPU)
make test        # Test streaming endpoint
curl -N http://localhost:8000/v1/chat/completions/stream \
  -H "Content-Type: application/json" \
  -d '{"model":"...", "prompt":"...", "max_tokens":100}'
```

### Task 3.3: Module 10 - Production Operations & Observability

**Dependencies:** Module 09, Prometheus/Grafana infrastructure

**Deliverables:**
- Golden Signals metrics (TTFT, TPOT, KV cache, perplexity)
- OpenTelemetry instrumentation
- Prometheus exporter for custom metrics
- Grafana dashboard definition
- Lab 2: Canary rollout with automated rollback

**Validation:**
```bash
cd 10-production-operations-observability
make up          # Start metrics + vLLM
make test        # Collect golden signals
make validate    # Check dashboard in Grafana
./labs/lab_2_canary_rollout.py
```

### Task 3.4: Module 16 - Hands-On Labs (All Three)

**Dependencies:** Modules 08, 10, 11

**Deliverables:**
- Lab 1 (in Module 08): VRAM Budgeting & QLLoRA Sizing
  - Calculator script
  - Solutions with architectural derivation
  - Automated grader
- Lab 2 (in Module 10): Canary Deployment & Rollback
  - Test prompt generation
  - Hallucination rate monitoring
  - Automated rollback logic
- Lab 3 (in Module 11): Prompt Template Skew Detection
  - Jinja template validation
  - Tokenizer fidelity check
  - Unit test suite

**Validation:**
```bash
cd 16-hands-on-labs
make test        # Run all lab harnesses
./test_lab_1.py && ./test_lab_2.py && ./test_lab_3.py
```

---

## Phase 4: Safety, Governance & Operations (Week 4)

Build order: **11 → 12 → 13 → 14 → 15 → 19**

### Task 4.1: Module 11 - Prompt Management & Train-Serve Skew

**Dependencies:** Module 10

**Deliverables:**
- Centralized Prompt Registry (Postgres-backed)
- Pydantic v2 contract validator
- Jinja2 template linting
- Zero-skew detector (byte-for-byte tokenizer comparison)
- Lab 3: Prompt template CI test

**Validation:**
```bash
cd 11-prompt-management-train-serve-skew
make up
make test        # Verify zero-skew detection
./labs/test_lab_3.py
```

### Task 4.2: Module 12 - Safety & Responsible AI

**Dependencies:** Module 11

**Deliverables:**
- Ingress guardrail: Prompt injection detector
- Ingress guardrail: PII anonymizer
- Egress guardrail: Hallucination checker
- Multi-tier architecture (4 layers)
- Safety evaluator using LLM-as-Judge

**Validation:**
```bash
cd 12-safety-responsible-ai
make test        # Test all guardrails
make validate    # Functional tests
```

### Task 4.3: Module 13 - Risk Evaluation

**Dependencies:** Module 12

**Deliverables:**
- 2x2 risk matrix (Probability vs Severity)
- Dynamic thresholding logic
- Escalation workflows
- Context-aware routing

**Validation:**
```bash
cd 13-risk-evaluation-probability-severity
make test
```

### Task 4.4: Module 14 - LLMOps vs LLM System Design

**Dependencies:** Module 13

**Deliverables:**
- Demarcation of responsibilities table
- Infrastructure vs Application architecture separation
- Hybrid RAG with Reciprocal Rank Fusion example
- Hybrid BM25 + Vector search implementation

**Validation:**
```bash
cd 14-llmops-vs-llm-system-design
make test
```

### Task 4.5: Module 15 - Beyond the Course

**Dependencies:** Module 14

**Deliverables:**
- RAGAS evaluation framework integration
- DeepEval LLM unit testing
- LangGraph agents example
- Platform engineering guide

**Validation:**
```bash
cd 15-beyond-the-course
make test        # Test evaluation frameworks
```

### Task 4.6: Module 19 - Enterprise Production Checklist

**Dependencies:** All previous modules

**Deliverables:**
- Full readiness checklist (data, inference, prompts, safety, telemetry)
- `readiness_audit.py` script that probes all components
- `validation_report.py` generator
- Verification report output

**Validation:**
```bash
cd 19-production-checklist
python src/readiness_audit.py
python src/validation_report.py
```

---

## Phase 5: Concept & Reference Modules (Throughout)

These can be built in parallel (no execution required):

### Module 01: What is LLMOps?
- Paradigm shift visualization
- 9 Pillars interactive explanation
- Conceptual overview notebook

### Module 02: MLOps to LLMOps Framework
- 7-stage lifecycle diagram
- Naive deployment anti-pattern script
- Exercise 2.1: Gap assessment

### Module 17: Interview Preparation
- 25 Q&As with deep-dive answers
- One module per question
- Practice tests

### Module 18: Comprehensive Glossary
- 60+ terms organized by category
- Reference material

---

## Validation Strategy

Each module implements three targets:

```bash
make up          # Start services for this module
make test        # Run pytest suite (unit + integration tests)
make validate    # Health checks + functional validation
make down        # Cleanup containers
make reset       # Hard reset (remove volumes)
```

### Golden Path Testing

After building each module, run the integration test:

```bash
cd <module-folder>
make up
make validate      # Should output: "✓ All validations passed"
make down
```

### Module Interdependency Tests

After building all modules, run end-to-end:

```bash
# Infrastructure
make infra-up
make infra-validate

# Build order: 03 → 04 → 05 → 07 → 08 → 06 → 09 → 10 → 16
for module in 03 04 05 07 08 06 09 10 11 12 13 14 15 16; do
  cd "$module-*"
  make up
  make validate || exit 1
  make down
  cd ..
done

# Final: Production checklist
cd 19-production-checklist
python src/readiness_audit.py
```

---

## Dependency Graph

```
infra (shared services)
  ├─ 03 (Data Prep)
  │   ├─ 04 (Lineage)
  │   │   ├─ 05 (Fine-Tuning)
  │   │   │   ├─ 07 (Artifacts)
  │   │   │   │   ├─ 08 (LoRA/QLoRA)
  │   │   │   │   │   ├─ 09 (Serving)
  │   │   │   │   │   │   ├─ 10 (Observability)
  │   │   │   │   │   │   │   ├─ 11 (Prompts)
  │   │   │   │   │   │   │   │   ├─ 12 (Safety)
  │   │   │   │   │   │   │   │   │   ├─ 13 (Risk)
  │   │   │   │   │   │   │   │   │   │   ├─ 14 (Design)
  │   │   │   │   │   │   │   │   │   │   │   ├─ 15 (Frontier)
  │   │   │   │   │   │   │   │   │   │   │   │   └─ 19 (Checklist)
  │   │   │   │   │   │   │   │   │   │   │   │       └─ 16 (Labs)
```

---

## Estimated Timeline

| Phase | Modules | Duration | Status |
|---|---|---|---|
| **Foundation** | Infrastructure | 3-4 hours | In Progress |
| **Data Pipeline** | 03-05, 07-08 | 16-20 hours | Pending |
| **Orchestration & Serving** | 06, 09-10, 16 | 16-20 hours | Pending |
| **Safety & Governance** | 11-15, 19 | 16-20 hours | Pending |
| **Concept Modules** | 01-02, 17-18 | 8-12 hours | Pending |
| **Total** | All 19 modules | **60-80 hours** | |

---

## Key Success Metrics

✅ All modules have passing `make validate`  
✅ All 19 chapters from the PDF are covered with working code  
✅ All hands-on labs (1, 2, 3) have automated graders  
✅ All 25 interview questions are answered  
✅ All 60+ glossary terms are documented  
✅ Enterprise checklist probes all components successfully  
✅ End-to-end validation passes without errors  

---

**Next Steps:**

1. ✅ Infrastructure up and running
2. → Start Module 03 (Scalable Data Preparation)
3. Continue build order sequentially
4. Validate each module before proceeding
5. Complete all 19 modules
6. Run final enterprise checklist validation

