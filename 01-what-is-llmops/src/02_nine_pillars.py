"""
Module 01: The Nine Core Pillars of LLMOps

This script explains and demonstrates each of the 9 foundational pillars
that production-grade LLMOps systems must implement.
"""

from typing import Dict, List
from dataclasses import dataclass


@dataclass
class Pillar:
    """Framework for explaining each LLMOps pillar"""
    number: int
    name: str
    description: str
    why_matters: str
    technologies: List[str]
    production_checklist: List[str]

    def __str__(self):
        tech_str = "\n    • ".join(self.technologies)
        checklist_str = "\n    ☐ ".join(self.production_checklist)

        return f"""
╔════════════════════════════════════════════════════════════════╗
║  PILLAR {self.number}: {self.name}
╚════════════════════════════════════════════════════════════════╝

Description:
{self._wrap_text(self.description, 70)}

Why It Matters:
{self._wrap_text(self.why_matters, 70)}

Key Technologies:
    • {tech_str}

Production Readiness Checklist:
    ☐ {checklist_str}
"""

    @staticmethod
    def _wrap_text(text: str, width: int) -> str:
        """Simple text wrapper"""
        lines = []
        words = text.split()
        current_line = []
        for word in words:
            if len(" ".join(current_line + [word])) <= width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append("  " + " ".join(current_line))
                current_line = [word]
        if current_line:
            lines.append("  " + " ".join(current_line))
        return "\n".join(lines)


def pillar_1_data_preparation():
    return Pillar(
        number=1,
        name="Data Preparation & Curation",
        description=(
            "Ingesting unstructured text, removing PII, deduplicating via MinHash/LSH, "
            "filtering noise, and converting enterprise assets into instruction-tuning "
            "or vector search formats."
        ),
        why_matters=(
            "High-quality, deduplicated data is the foundation. A 10K example high-quality dataset "
            "outperforms 500K noisy samples. PII leakage creates legal liability. Duplicates inflate "
            "reported accuracy."
        ),
        technologies=[
            "DuckDB (distributed SQL pipelines)",
            "MinHash / LSH (deduplication)",
            "Pydantic (data validation)",
            "Great Expectations (data profiling)",
            "spaCy (NLP preprocessing)",
        ],
        production_checklist=[
            "Automated deduplication via SHA256 hashing",
            "PII detection and redaction (SSN, email, API keys)",
            "Token length validation (not too short, not too long)",
            "Data quality metrics logged to MLflow",
            "Version every dataset with git-commit-like hashing",
        ]
    )


def pillar_2_model_selection():
    return Pillar(
        number=2,
        name="Experimentation & Model Selection",
        description=(
            "Benchmarking commercial APIs (Gemini, Claude, GPT) against open-weights models "
            "(Llama-3, Mistral, Gamma) across cost, latency, license, and context window."
        ),
        why_matters=(
            "Model choice is 80% of the outcome. Picking the wrong model wastes months. "
            "Proprietary models have high quality but lock you in. Open models give control but "
            "require infrastructure."
        ),
        technologies=[
            "LMSys Chatbot Arena (crowdsourced benchmarks)",
            "MMLU / GSM8k / TruthfulQA (academic benchmarks)",
            "RAGAS / DeepEval (domain-specific evaluation)",
            "Model cards (Hugging Face Hub)",
        ],
        production_checklist=[
            "Evaluated at least 3 models (commercial + open-source)",
            "Benchmarked on task-specific golden dataset",
            "Documented cost/latency/accuracy trade-offs",
            "Established model selection criteria",
            "Can switch models within 24 hours",
        ]
    )


def pillar_3_prompt_management():
    return Pillar(
        number=3,
        name="Prompt Management & Versioning",
        description=(
            "Treating prompts, system instructions, few-shot examples, and output schemas "
            "as version-controlled artifacts with automated linting."
        ),
        why_matters=(
            "A single space or newline in a prompt changes model output. Without versioning, "
            "you cannot debug regressions or trace what changed. Train-serve skew happens when "
            "training prompts differ from serving prompts."
        ),
        technologies=[
            "Jinja2 templating",
            "Git (prompt versioning)",
            "Pydantic (schema validation)",
            "Prompt Registry (centralized, versioned)",
            "Automated fidelity checks",
        ],
        production_checklist=[
            "All prompts in Jinja2 format with required variables",
            "Prompts version-controlled in git with tags",
            "Automated linting: check for missing variables",
            "Zero train-serve skew: byte-for-byte tokenizer match",
            "Prompt templates validated in CI/CD before deploy",
        ]
    )


def pillar_4_fine_tuning():
    return Pillar(
        number=4,
        name="Fine-Tuning & Adaptation",
        description=(
            "Employing Parameter-Efficient Fine-Tuning (PEFT/LoRA/QLoRA) to adapt model "
            "style, domain vocabulary, or formatting without catastrophic forgetting."
        ),
        why_matters=(
            "Full fine-tuning requires 140GB VRAM for a 70B model. LoRA reduces trainable "
            "parameters to 0.25%, requiring only 12GB. Fine-tuning teaches style; RAG teaches facts."
        ),
        technologies=[
            "LoRA / QLoRA (parameter-efficient training)",
            "HuggingFace transformers",
            "PEFT library",
            "bitsandbytes (4-bit quantization)",
            "Gradient checkpointing",
        ],
        production_checklist=[
            "LoRA rank and alpha parameters tuned for domain",
            "Training on deduplicated, high-quality dataset",
            "Evaluation against baseline (golden dataset)",
            "Adapter weights versioned in MLflow",
            "Adapter can be swapped at runtime (S-LoRA)",
        ]
    )


def pillar_5_high_throughput_serving():
    return Pillar(
        number=5,
        name="High-Throughput Deployment & Serving",
        description=(
            "Leveraging modern inference runtimes (vLLM, TensorRT-LLM, Triton) with "
            "PagedAttention and continuous batching for <30ms per-token latency."
        ),
        why_matters=(
            "Naive Flask wrappers cause sequential bottlenecks. KV cache fragmentation wastes "
            "60–80% of GPU VRAM. PagedAttention reduces waste to <4%, enabling 4x–24x throughput."
        ),
        technologies=[
            "vLLM (with PagedAttention)",
            "TensorRT-LLM (production)",
            "Triton Inference Server",
            "FastAPI (async HTTP)",
            "Ollama (CPU-friendly)",
        ],
        production_checklist=[
            "TTFT (Time-to-First-Token) < 350ms",
            "TPOT (Time-Per-Output-Token) < 30ms",
            "Async streaming API (Server-Sent Events)",
            "Request queuing with SLA enforcement",
            "Graceful degradation under load",
        ]
    )


def pillar_6_observability():
    return Pillar(
        number=6,
        name="Continuous Monitoring & Observability",
        description=(
            "Tracking operational metrics (TTFT, TPOT, GPU VRAM, queue delays) alongside "
            "semantic quality metrics (hallucination rate, answer relevancy, perplexity)."
        ),
        why_matters=(
            "Ops team doesn't know if output is correct; ML team doesn't know if latency is good. "
            "Both need unified observability. Golden Signals catch issues before users notice."
        ),
        technologies=[
            "Prometheus (metrics collection)",
            "Grafana (dashboards)",
            "OpenTelemetry (distributed tracing)",
            "Jaeger (trace visualization)",
            "Custom semantic metrics (LLM-as-Judge)",
        ],
        production_checklist=[
            "Prometheus scraping vLLM metrics",
            "Grafana dashboard for Golden Signals",
            "OpenTelemetry instrumentation on all inference paths",
            "Automated alerts on TTFT > 350ms or TPOT > 30ms",
            "Semantic quality metrics logged (hallucination rate, similarity)",
        ]
    )


def pillar_7_safety():
    return Pillar(
        number=7,
        name="Safety, Moderation & Responsible AI",
        description=(
            "Deploying multi-layered guardrails to intercept jailbreaks, prompt injections, "
            "toxic generations, and data leakage."
        ),
        why_matters=(
            "LLMs act as code interpreters for natural language; inputs are untrusted. "
            "Jailbreaks, prompt injections, and data exfiltration are real threats. "
            "Multi-tier guardrails reduce risk."
        ),
        technologies=[
            "Llama Guard (safety classification)",
            "Prompt injection detectors",
            "PII redaction (regex + ML)",
            "NeMo Guardrails (business logic)",
            "Output semantic validators",
        ],
        production_checklist=[
            "Ingress guardrail: Detect and block prompt injections",
            "Semantic policy layer: Enforce business rules",
            "Egress guardrail: Detect hallucinations and data leakage",
            "Multi-tier safety (4 layers minimum)",
            "Safety metrics logged and monitored",
        ]
    )


def pillar_8_orchestration():
    return Pillar(
        number=8,
        name="Workflow Orchestration",
        description=(
            "Running automated Directed Acyclic Graphs (DAGs) using Kubeflow Pipelines, "
            "Airflow, or Argo to schedule data refreshes, adapter training, and benchmarks."
        ),
        why_matters=(
            "Jupyter notebooks are research sandboxes; production requires reproducible DAGs. "
            "DAGs provide strongly-typed inputs/outputs, retries, conditional branching, "
            "and CI/CD integration."
        ),
        technologies=[
            "Kubeflow Pipelines v2 (Kubernetes-native)",
            "Apache Airflow (general-purpose DAGs)",
            "GitHub Actions (CI/CD pipelines)",
            "Argo Workflows",
        ],
        production_checklist=[
            "End-to-end pipeline: Extract → Tokenize → Train → Evaluate → Deploy",
            "Typed component inputs/outputs",
            "Conditional gates (e.g., IF accuracy > 0.92 THEN deploy)",
            "Automated regression testing (golden dataset)",
            "Pipeline versioning and reproducibility",
        ]
    )


def pillar_9_automation():
    return Pillar(
        number=9,
        name="Automation & Continuous Alignment (CI/CD/CT)",
        description=(
            "Automating deployment gates, canary routing, and preference alignment via "
            "Direct Preference Optimization (DPO) and human-in-the-loop feedback."
        ),
        why_matters=(
            "Manual deployments are error-prone and slow. Canary routing (10% traffic) catches "
            "issues before full rollout. User feedback enables continuous improvement via DPO."
        ),
        technologies=[
            "GitHub Actions / GitLab CI (CI/CD)",
            "Kubernetes / Istio (canary routing)",
            "Direct Preference Optimization (DPO)",
            "Feedback loop aggregation",
        ],
        production_checklist=[
            "Automated gate: Deploy only if golden metrics pass",
            "Canary routing: 10% traffic for 1 hour, monitor hallucination",
            "Automatic rollback on anomaly detection",
            "User feedback collection (thumbs-up/-down)",
            "Continuous training loop using collected feedback",
        ]
    )


def print_pillar_dependencies():
    """Show how the 9 pillars depend on each other"""
    print("\n" + "=" * 70)
    print("PILLAR INTERDEPENDENCIES")
    print("=" * 70)
    print("""
The 9 pillars are NOT independent; weaknesses cascade:

  Pillar 1 (Data) → Pillar 2 (Model Selection)
    ↓
  Pillar 3 (Prompts) → Pillar 4 (Fine-Tuning)
    ↓
  Pillar 5 (Serving) → Pillar 6 (Observability)
    ↓
  Pillar 7 (Safety) ← Pillar 6 (detects issues)
    ↓
  Pillar 8 (Orchestration) ← All above (automates)
    ↓
  Pillar 9 (Automation) ← Pillars 6-8 (gates on metrics)

Example Chain Failure:
  If you skip Pillar 1 (bad data):
    → Model Selection (Pillar 2) picks wrong model because data is noisy
    → Fine-Tuning (Pillar 4) fails to improve (garbage in, garbage out)
    → Serving (Pillar 5) has high hallucination rate
    → Observability (Pillar 6) detects the problem too late
    → Safety (Pillar 7) flags outputs as toxic
    → Orchestration (Pillar 8) blocks deployment
    → Automation (Pillar 9) alerts on-call engineer at 3am

Prevention: Invest in Pillar 1 first!
""")


def print_production_readiness_assessment():
    """Help assess if your system has all 9 pillars"""
    print("\n" + "=" * 70)
    print("PRODUCTION READINESS: 9 PILLARS ASSESSMENT")
    print("=" * 70)
    print("""
Rate each pillar: ✓ (Yes) / ◐ (Partial) / ✗ (No)

Pillar 1: Data Preparation & Curation
  ☐ Automated deduplication (SHA256 hashing)
  ☐ PII scrubbing
  ☐ Token length validation
  ☐ Versioned datasets with manifests
  [Your score: ____ / 4]

Pillar 2: Experimentation & Model Selection
  ☐ Benchmarked multiple models
  ☐ Trade-off analysis (cost/latency/accuracy)
  ☐ Model selection criteria documented
  ☐ Can swap models in < 24 hours
  [Your score: ____ / 4]

Pillar 3: Prompt Management & Versioning
  ☐ Prompts in git with version tags
  ☐ Jinja2 templating with required variables
  ☐ Automated linting
  ☐ Zero train-serve skew (byte-for-byte)
  [Your score: ____ / 4]

Pillar 4: Fine-Tuning & Adaptation
  ☐ LoRA/QLoRA setup for domain adaptation
  ☐ Training on high-quality dataset
  ☐ Evaluation against baseline
  ☐ Adapter versioning in MLflow
  [Your score: ____ / 4]

Pillar 5: High-Throughput Deployment & Serving
  ☐ Using vLLM / TensorRT-LLM (not Flask)
  ☐ Streaming API (SSE)
  ☐ TTFT < 350ms
  ☐ TPOT < 30ms
  [Your score: ____ / 4]

Pillar 6: Continuous Monitoring & Observability
  ☐ Prometheus + Grafana setup
  ☐ Golden Signals dashboard (TTFT, TPOT, KV cache)
  ☐ OpenTelemetry tracing
  ☐ Semantic quality metrics logged
  [Your score: ____ / 4]

Pillar 7: Safety, Moderation & Responsible AI
  ☐ Ingress guardrail (prompt injection detector)
  ☐ PII anonymizer
  ☐ Egress guardrail (hallucination check)
  ☐ Multi-tier safety (4 layers)
  [Your score: ____ / 4]

Pillar 8: Workflow Orchestration
  ☐ End-to-end DAG (Extract → Train → Evaluate → Deploy)
  ☐ Typed component inputs/outputs
  ☐ Automated regression testing
  ☐ Conditional deployment gates
  [Your score: ____ / 4]

Pillar 9: Automation & Continuous Alignment
  ☐ Automated deployment gates
  ☐ Canary routing (10% traffic)
  ☐ Automatic rollback on anomaly
  ☐ Feedback loop setup
  [Your score: ____ / 4]

TOTAL SCORE: ____ / 36

Interpretation:
  36: Production-ready LLMOps system ✓
  28–35: Most pillars implemented, some gaps
  20–27: Significant gaps; focus on missing pillars
  < 20: Early-stage; need foundational work (prioritize Pillars 1–3)
""")


def main():
    """Run all demonstrations"""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "  MODULE 01: THE NINE CORE PILLARS OF LLMOPS  ".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "═" * 68 + "╝")

    # Display all 9 pillars
    pillars = [
        pillar_1_data_preparation(),
        pillar_2_model_selection(),
        pillar_3_prompt_management(),
        pillar_4_fine_tuning(),
        pillar_5_high_throughput_serving(),
        pillar_6_observability(),
        pillar_7_safety(),
        pillar_8_orchestration(),
        pillar_9_automation(),
    ]

    for pillar in pillars:
        print(pillar)

    # Show dependencies
    print_pillar_dependencies()

    # Show assessment tool
    print_production_readiness_assessment()

    print("\n" + "=" * 70)
    print("✓ Nine Pillars explanation complete")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
