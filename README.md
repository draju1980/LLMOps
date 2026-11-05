# LLMOps Complete Course - Open-Source, Docker-Based Implementation

A comprehensive, production-grade LLMOps engineering curriculum with hands-on labs, fully executable on local machines using open-source technologies and Docker.

**Edition:** 2026 Production Edition (Adapted from "LLMOps Complete Course Guide")  
**Target Runtimes:** vLLM, TensorRT-LLM, Kubeflow Pipelines, PyTorch, LoRA, QLoRA  
**Platform:** Fully local, no cloud services required  
**Hardware:** Tested on arm64 (Apple Silicon) with 48GB+ RAM and Docker

---

## Quick Start

```bash
# Clone and navigate
git clone <this-repo>
cd LLMOps

# View the course structure
tree -L 2 -I '__pycache__|*.pyc'

# Run Module 1 (Introduction)
cd 01-what-is-llmops
make up          # Start all services
make validate    # Verify setup
make lab         # Run hands-on exercises

# View all available modules
ls -d [0-9][0-9]-*/
```

---

## Technology Replacement Map

| Original (Google Cloud / Proprietary) | Local Open-Source Replacement | Why This Choice | Docker Image Tag |
|---|---|---|---|
| **BigQuery** | DuckDB + Parquet | OLAP queries, embedded, zero infrastructure | `duckdb/duckdb:v1.0.0` |
| **GCS** | MinIO | S3-compatible object storage, self-hosted | `minio/minio:latest` |
| **Model Registry** | MLflow + Postgres + MinIO | Artifact versioning, experiment tracking | `ghcr.io/mlflow/mlflow:v2.14.1` |
| **Monitoring** | Prometheus + Grafana | Metrics collection, alerting, dashboards | `prom/prometheus:v2.55.1` + `grafana/grafana:11.0.0` |
| **Distributed Tracing** | OpenTelemetry Collector + Jaeger | Full request tracing, latency analysis | `otel/opentelemetry-collector:v0.99.0` + `jaegertracing/all-in-one:v1.54` |
| **LangSmith / Evaluations** | Langfuse (self-hosted) or Phoenix | Observability for LLM chains | `ghcr.io/langfuse/langfuse:latest` |
| **Semantic Cache** | Redis | In-memory KV cache for prompt embeddings | `redis:7.4-alpine` |
| **Vector Database** | Qdrant | Scalable vector/semantic search | `qdrant/qdrant:v1.8.0` |
| **Keyword Search (BM25)** | `rank_bm25` Python library | Fast sparse retrieval | N/A (pip package) |
| **LLM Judge / Safety** | Local Llama Guard 3 (7B) behind same vLLM endpoint | Self-hosted, zero external API calls | `ollama/ollama:latest` or vLLM |
| **Inference Engine (vLLM)** | vLLM with CPU fallback | High-throughput, PagedAttention, async | `vllm/vllm:v0.5.0` |
| **Model Serving Baseline** | Ollama or llama.cpp-server | CPU-friendly, arm64-native | `ollama/ollama:latest` |
| **Orchestration** | Kubeflow Pipelines v2 (with local docker runner) or Airflow | DAGs with typed components | `python:3.11-slim` + `apache/airflow:2.10.0` |
| **Database** | PostgreSQL | Experiment tracking, metadata | `postgres:16-alpine` |
| **Message Broker** | Redis or Celery | Task queues, async workers | `redis:7.4-alpine` |

**Note:** All images are pinned to specific versions for reproducibility. Docker Compose profiles (e.g., `--profile gpu`, `--profile local-llm`) control which services start.

---

## Course Structure

```
LLMOps/
├── README.md                          # This file
├── .gitignore                         # Excludes .claude, data/, models/, etc.
├── docker-compose.yml                 # Shared infrastructure (profiles: gpu, local-llm)
├── infra/
│   ├── Dockerfile.base                # Base Python 3.11 image with common deps
│   ├── docker-compose.infra.yml       # Postgres, MinIO, Redis, etc.
│   ├── config/
│   │   ├── prometheus.yml             # Metrics scrape config
│   │   ├── grafana/dashboards/        # Pre-built Golden Signals dashboard
│   │   └── jaeger-config.json         # Tracing configuration
│   └── scripts/
│       ├── init-minio.sh              # Create MinIO buckets
│       ├── init-postgres.sh           # Initialize databases
│       └── validate-stack.sh           # Health checks
│
├── docs/
│   ├── source-outline.md              # Complete PDF content (code blocks, tables, Q&As)
│   ├── IMPLEMENTATION_PLAN.md         # Detailed chapter-by-chapter plan
│   └── GLOSSARY.md                    # 60+ LLMOps terms
│
├── 01-what-is-llmops/
│   ├── README.md                      # Learning objectives, concepts
│   ├── Makefile                       # up, down, reset, validate, lab targets
│   ├── docker-compose.yml             # This module's services
│   ├── src/
│   │   ├── 01_paradigm_shift.py       # DevOps → MLOps → LLMOps evolution
│   │   └── 02_nine_pillars.py         # Interactive explanation of 9 core pillars
│   └── notebooks/
│       └── 01_conceptual_overview.ipynb # Jupyter for interactive learning
│
├── 02-mlops-to-llmops-framework/
│   ├── README.md
│   ├── Makefile
│   ├── docker-compose.yml
│   ├── src/
│   │   ├── naive_deployment.py        # Anti-pattern (raw transformers on EC2)
│   │   └── solution_lifecycle_gap.py  # Solution with 4 critical components
│   └── exercises/
│       └── exercise_2_1.md            # Hands-on gap assessment
│
├── 03-scalable-data-preparation/
│   ├── README.md
│   ├── Makefile
│   ├── docker-compose.yml
│   ├── src/
│   │   ├── duckdb_elt_pipeline.py     # Enterprise SQL pipeline (DuckDB)
│   │   ├── data_validation.py         # Pydantic schemas, PII scrubbing
│   │   └── deduplication.py           # SHA256 hashing, MinHash LSH
│   ├── data/
│   │   ├── sample_support_tickets.csv # Few hundred rows for testing
│   │   └── download.sh                 # Full dataset download script
│   └── tests/
│       └── test_elt_pipeline.py       # Validates SQL correctness
│
├── 04-dataset-engineering-lineage/
│   ├── README.md
│   ├── Makefile
│   ├── docker-compose.yml
│   ├── src/
│   │   ├── dataset_manifest.py        # SHA256 hashing, immutability
│   │   ├── lineage_dag.py             # Provenance tracking
│   │   └── train_val_test_split.py    # Leakage prevention
│   ├── manifests/
│   │   └── support_v1_sha256_8f9a2.json # Example manifest
│   └── labs/
│       └── lab_dataset_versioning.py
│
├── 05-fine-tuning-data-engineering/
│   ├── README.md
│   ├── Makefile
│   ├── docker-compose.yml
│   ├── src/
│   │   ├── chatml_formatter.py        # ChatML, Alpaca, Llama-3 formats
│   │   ├── instruction_structuring.py # Prompt-Input-Response construction
│   │   └── loss_masking.py            # Labels = -100 on prompt tokens
│   ├── data/
│   │   └── sample_instructions.jsonl  # Few examples in ChatML format
│   └── tests/
│       └── test_loss_masking.py       # Verifies only response tokens trained
│
├── 06-kubeflow-pipelines/
│   ├── README.md
│   ├── Makefile
│   ├── docker-compose.yml             # KFP + Postgres (metadata store)
│   ├── src/
│   │   ├── llm_training_pipeline.py   # KFP v2 DAG with @dsl.component
│   │   ├── components/
│   │   │   ├── extract_data.py        # Component 1: Data extraction
│   │   │   ├── tokenize_mask.py       # Component 2: ChatML formatting
│   │   │   ├── train_lora.py          # Component 3: LoRA training
│   │   │   └── evaluate_model.py      # Component 4: Evaluation
│   │   └── runner.py                  # Compiles & executes pipeline locally
│   ├── pipelines/
│   │   └── llm_pipeline.yaml          # Compiled KFP manifest
│   └── tests/
│       └── test_pipeline_execution.py
│
├── 07-artifact-management-versioning/
│   ├── README.md
│   ├── Makefile
│   ├── docker-compose.yml             # MLflow server
│   ├── src/
│   │   ├── model_card_schema.py       # README.md + lineage metadata
│   │   ├── artifact_registry.py       # MLflow integration
│   │   └── adapter_versioning.py      # LoRA artifact lineage
│   ├── artifacts/
│   │   └── example_model_card.md      # Full artifact lineage example
│   └── tests/
│       └── test_artifact_versioning.py
│
├── 08-peft-lora-qlora/
│   ├── README.md
│   ├── Makefile
│   ├── docker-compose.yml
│   ├── src/
│   │   ├── lora_math.py               # W = W₀ + (α/r)(B × A)
│   │   ├── lora_training_simple.py    # CPU-friendly: SmolLM2-135M + LoRA
│   │   ├── qlora_training.py          # GPU profile: NF4 + QLoRA on 14B
│   │   └── vram_calculator.py         # Lab 1 calculator
│   ├── models/
│   │   └── .gitkeep                   # Downloaded models cached here
│   ├── labs/
│   │   ├── lab_1_vram_budgeting.py    # VRAM calculation exercise
│   │   ├── lab_1_solution.md          # Expected output
│   │   └── test_lab_1.py              # Automated grading
│   └── tests/
│       └── test_lora_training.py
│
├── 09-model-deployment-serving/
│   ├── README.md
│   ├── Makefile
│   ├── docker-compose.yml             # vLLM (or Ollama for CPU)
│   ├── src/
│   │   ├── naive_flask_server.py      # ❌ Anti-pattern (why it fails)
│   │   ├── production_fastapi_vllm.py # ✅ Production FastAPI + vLLM + streaming
│   │   ├── llm_engine.py              # Async LLMEngine wrapper
│   │   └── sampling_params.py         # Temperature, top-p, max_tokens
│   ├── tests/
│   │   └── test_streaming_response.py
│   └── integration-tests/
│       └── test_e2e_serving.py        # Curl-based streaming validation
│
├── 10-production-operations-observability/
│   ├── README.md
│   ├── Makefile
│   ├── docker-compose.yml             # Prometheus, Grafana, OpenTelemetry
│   ├── src/
│   │   ├── golden_signals.py          # TTFT, TPOT, KV cache, perplexity metrics
│   │   ├── opentelemetry_instrumentation.py # OTel integration
│   │   ├── prometheus_exporter.py     # Custom metrics
│   │   └── canary_monitoring.py       # Deployment validation
│   ├── dashboards/
│   │   └── golden_signals.json        # Grafana dashboard definition
│   └── labs/
│       └── lab_2_canary_rollout.py    # End-to-end canary with rollback
│
├── 11-prompt-management-train-serve-skew/
│   ├── README.md
│   ├── Makefile
│   ├── docker-compose.yml
│   ├── src/
│   │   ├── prompt_registry.py         # Centralized versioned prompt management
│   │   ├── prompt_contract.py         # Pydantic v2 validation
│   │   ├── jinja_linting.py           # Detects missing required_variables
│   │   └── train_serve_skew_detector.py # Byte-for-byte tokenizer comparison
│   ├── prompts/
│   │   ├── enterprise_support.v1.2.0.jinja2
│   │   ├── financial_analyst.v2.0.0.jinja2
│   │   └── prompt_index.json          # Registry manifest
│   ├── tests/
│   │   └── test_zero_skew.py          # Ensures exact token match
│   └── labs/
│       └── lab_3_prompt_skew_detection.py
│
├── 12-safety-responsible-ai/
│   ├── README.md
│   ├── Makefile
│   ├── docker-compose.yml
│   ├── src/
│   │   ├── ingress_guardrail.py       # Prompt injection detector, PII anonymizer
│   │   ├── egress_guardrail.py        # Hallucination, citation, jailbreak checks
│   │   ├── multi_tier_architecture.py # 4-layer safety stack
│   │   └── safety_evaluator.py        # LLM-as-Judge safety scoring
│   ├── patterns/
│   │   ├── injection_patterns.json    # Regex heuristics
│   │   └── pii_patterns.json          # PII detection rules
│   └── tests/
│       └── test_safety_middleware.py
│
├── 13-risk-evaluation-probability-severity/
│   ├── README.md
│   ├── Makefile
│   ├── src/
│   │   ├── risk_matrix.py             # Probability vs Severity 4-quadrant
│   │   ├── dynamic_thresholding.py    # Context-aware risk routing
│   │   └── escalation_workflow.py     # High-severity low-confidence handling
│   └── tests/
│       └── test_risk_matrix.py
│
├── 14-llmops-vs-llm-system-design/
│   ├── README.md
│   ├── Makefile
│   ├── src/
│   │   ├── infrastructure_layer.py    # LLMOps concerns (latency, cost, automation)
│   │   ├── application_layer.py       # LLM System Design (RAG, agents, UX)
│   │   └── hybrid_rag_rrf.py          # Reciprocal Rank Fusion example
│   └── notebooks/
│       └── system_design_patterns.ipynb
│
├── 15-beyond-the-course/
│   ├── README.md
│   ├── ragas_evaluation.py            # Retrieval-Augmented Generation Assessment
│   ├── deepeval_framework.py          # Unit-testing LLMs
│   ├── langgraph_agents.py            # Multi-agent orchestration
│   └── platform_engineering.md        # Building internal developer platforms
│
├── 16-hands-on-labs/
│   ├── README.md
│   ├── LAB_1_VRAM_BUDGETING.md        # Complete VRAM calculator + solutions
│   ├── LAB_2_CANARY_ROLLOUT.md        # Automated deployment validation + rollback
│   ├── LAB_3_PROMPT_SKEW.md           # Zero-skew prompt template detection
│   ├── src/
│   │   ├── lab_1_vram_calculator.py   # Answers in `solutions/`
│   │   ├── lab_2_canary_script.py     # Reference implementation
│   │   └── lab_3_prompt_validator.py  # Test harness
│   ├── solutions/
│   │   ├── lab_1_solution.md
│   │   ├── lab_2_solution.py
│   │   └── lab_3_solution.py
│   └── tests/
│       ├── test_lab_1.py
│       ├── test_lab_2.py
│       └── test_lab_3.py
│
├── 17-interview-preparation/
│   ├── README.md
│   ├── INTERVIEW_QA.md                 # 25 Q&As with deep-dive answers (from source-outline.md)
│   ├── src/
│   │   ├── question_001_paged_attention.py
│   │   ├── question_002_ttft_vs_tpot.py
│   │   └── ...                        # One module per question
│   └── practice_tests/
│       └── mock_interview_1.md
│
├── 18-glossary/
│   ├── README.md
│   └── GLOSSARY.md                    # 60+ terms (from source-outline.md)
│
├── 19-production-checklist/
│   ├── README.md
│   ├── ENTERPRISE_CHECKLIST.md         # Full readiness checklist
│   ├── src/
│   │   ├── readiness_audit.py         # Script to probe all components
│   │   └── validation_report.py       # Generates audit report
│   └── tests/
│       └── test_checklist_items.py
│
└── IMPLEMENTATION_PLAN.md              # This document (build order, dependencies)
```

---

## Hardware & Prerequisites

### Minimum Requirements

- **CPU:** 4+ cores (arm64 or x86_64)
- **RAM:** 16GB (tested on 48GB arm64)
- **Disk:** 100GB+ (for models, datasets, Docker images)
- **Docker:** v29.0+
- **Docker Compose:** v2.25+

### Tested Platforms

- ✅ **macOS 14+** (Apple Silicon / arm64): Docker Desktop
- ✅ **Linux** (Ubuntu 22.04+, Debian 12+): Docker CE / Colima
- ✅ **Windows 11** (WSL2 + Docker Desktop): Supported
- ❌ **GPU:** Tested on CPU-only (arm64). GPU profiles provided for NVIDIA A100/RTX4090.

### Optional GPU Support

To enable GPU acceleration (NVIDIA GPUs only):
```bash
docker compose --profile gpu up -d
```
This pulls `vllm/vllm:v0.5.0-cu121` and enables CUDA-based quantization and inference.

---

## Module Overview & Learning Path

| # | Module | Focus | Duration | Dependencies |
|---|---|---|---|---|
| **1** | What is LLMOps? | Concepts, 9 pillars, paradigm shift | 2 hours | None |
| **2** | MLOps to LLMOps Framework | 7-stage lifecycle, hands-on gap assessment | 2 hours | 01 |
| **3** | Scalable Data Preparation | SQL pipelines, ELT, deduplication | 4 hours | 02, DuckDB |
| **4** | Dataset Engineering & Lineage | SHA256 versioning, DAGs, leakage prevention | 3 hours | 03 |
| **5** | Fine-Tuning Data Engineering | ChatML, loss masking, instruction formatting | 3 hours | 04 |
| **6** | Kubeflow Pipelines | KFP v2, DAGs, component containers | 4 hours | 05, Python, Docker |
| **7** | Artifact Management & Versioning | Model cards, MLflow, lineage tracking | 3 hours | 06, PostgreSQL |
| **8** | PEFT: LoRA & QLoRA | Mathematics, training scripts, VRAM budgeting | 5 hours | 07, PyTorch |
| **9** | Model Deployment & Serving | FastAPI, vLLM, streaming, async | 4 hours | 08, vLLM |
| **10** | Operations & Observability | Golden Signals, OpenTelemetry, Prometheus | 4 hours | 09, Grafana |
| **11** | Prompt Management & Train-Serve Skew | Prompt Registry, Jinja templates, linting | 3 hours | 10 |
| **12** | Safety & Responsible AI | Guardrails, prompt injection, PII scrubbing | 4 hours | 11 |
| **13** | Risk Evaluation: Probability vs Severity | Risk matrices, dynamic thresholding | 2 hours | 12 |
| **14** | LLMOps vs LLM System Design | Infrastructure vs application architecture | 2 hours | 13 |
| **15** | Beyond the Course: Modern Frontier | RAGAS, DeepEval, LangGraph, Platform Eng | 3 hours | 14 |
| **16** | Hands-on Labs & Exercises | Lab 1, 2, 3 (comprehensive practical) | 6 hours | 08, 10, 11 |
| **17** | Interview Preparation | 25 Q&As with deep-dive technical answers | Self-paced | 01-14 |
| **18** | Comprehensive Glossary | 60+ LLMOps terms and concepts | Reference | All |
| **19** | Production Checklist | Enterprise readiness assessment | 1 hour | All |

---

## Getting Started

### 1. Clone and Setup

```bash
git clone https://github.com/your-org/llmops-course.git
cd LLMOps
make infra-up       # Start shared infrastructure (Postgres, MinIO, Redis, etc.)
make infra-validate # Health checks
```

### 2. Run Your First Module

```bash
# Module 1: Introduction to LLMOps
cd 01-what-is-llmops
make up             # Start services (lightweight)
make validate       # Verify container health
make lab            # Run interactive exercises
make down           # Cleanup
```

### 3. Follow the Learning Path

Each module is self-contained:
```bash
cd <module-folder>
make up          # Start services defined in docker-compose.yml
make lab         # Run hands-on exercises
make validate    # Verify correctness
make down        # Cleanup containers
make reset       # Clean volumes & start fresh
```

---

## Validation & Testing

Every module includes automated tests:

```bash
cd 03-scalable-data-preparation
make test        # Run pytest suite
make validate    # Health checks + functional tests
```

All modules validate against:
- ✅ Container health (ports, logs, startup)
- ✅ Data correctness (SQL output, hashes, counts)
- ✅ Code behavior (unit + integration tests)
- ✅ Production readiness (checklist items)

---

## Architecture Decisions

### Why DuckDB over BigQuery?

- **DuckDB:** Embedded OLAP, Parquet native, SQL standard, zero infrastructure, free
- **BigQuery:** Cloud-bound, proprietary SQL dialect, requires authentication, $$

For this course, DuckDB runs in every module and can scale to TBs of Parquet files locally.

### Why Ollama / llama.cpp for Baseline Serving?

On arm64 (Apple Silicon), CPU-based inference is fast enough for 7B-13B models. vLLM requires CUDA, so we provide:
- **Default:** Ollama (arm64-native, easy setup)
- **Optional (GPU):** vLLM with `--profile gpu`

### Why Kubeflow Pipelines v2 with Local Docker Runner?

Full Kubernetes is production overkill for a local course. KFP v2 supports:
- **Local Docker runner:** Every `@dsl.component` runs as a local container
- **Full DAG semantics:** Strongly typed inputs/outputs, retries, caching
- **Kubernetes export:** Compiled YAML can deploy to real clusters

### Why PostgreSQL for Metadata?

- MLflow experiment tracking
- KFP pipeline metadata store
- Prompt Registry versioning
- Simple, ubiquitous, container-friendly

---

## Contributing & Extending

To add a new lab or extend a module:

1. **Follow the template:** Copy `[XX]-template/` structure
2. **Document thoroughly:** Every README includes Learning Objectives, Prerequisites, Concepts, Hands-on Exercises, Solutions, Troubleshooting
3. **Add tests:** Every lab must pass `make validate` and `make test`
4. **Pin versions:** All Docker images, Python packages, and models must be pinned
5. **Test locally first:** Validate on arm64 (macOS) and x86_64 (Linux)

---

## Troubleshooting

### Docker Memory Issues
```bash
# Increase Docker Desktop memory to 16GB+
# macOS: Docker Desktop → Preferences → Resources
# Linux: Edit /etc/docker/daemon.json
```

### Port Conflicts
Each module uses unique ports. View mappings:
```bash
grep -r "ports:" 0[0-9]-*/docker-compose.yml
```

### Model Download Failures
```bash
# Retry with verbose output
python -c "from transformers import AutoModel; AutoModel.from_pretrained('smollm2-135m')"
```

### OOM on Download
Some models are large. Use a machine with 32GB+ RAM, or download in a VM.

---

## References & Attribution

- **Original Course:** LLMOps Complete Course Guide (2026 Production Edition)
- **Framework:** Adapted from Google Cloud's MLOps curriculum
- **Open-Source Libraries:** vLLM, Ollama, DuckDB, Kubeflow, MLflow, Prometheus, Grafana, OpenTelemetry
- **Models:** Meta Llama, Mistral, SmolLM, Qwen (Hugging Face Hub)

---

## License

This course material is provided for educational purposes. Always check the licenses of underlying open-source projects and models.

---

**Happy Learning! 🚀**

For detailed module guides, start with `01-what-is-llmops/README.md`.
