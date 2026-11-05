"""
Module 01: Paradigm Shift - DevOps → MLOps → LLMOps

This script demonstrates the fundamental shifts in software engineering from
DevOps to MLOps to LLMOps, highlighting the challenges and requirements of each era.
"""

from dataclasses import dataclass
from typing import Dict, Any, List
import json


@dataclass
class ParadigmShift:
    """Framework for comparing software engineering paradigms"""
    era: str
    artifact: str
    determinism: str
    testing: str
    monitoring: str
    example: str

    def __str__(self):
        return f"""
╔════════════════════════════════════════════════════════════════╗
║  {self.era.upper()}
╚════════════════════════════════════════════════════════════════╝

Artifact:           {self.artifact}
Determinism:        {self.determinism}
Testing Strategy:   {self.testing}
Monitoring:         {self.monitoring}

Example:
{self.example}
"""


def devops_era():
    """2000s-2010s: Code-driven software engineering"""
    return ParadigmShift(
        era="DevOps (Code)",
        artifact="Compiled binaries, CI/CD pipelines, containers",
        determinism="Fully deterministic: Same input → Same output (always)",
        testing="Unit tests, integration tests, Boolean assertions",
        monitoring="Uptime, latency, error rate, resource utilization",
        example="""
def grant_access(user_id: int, user_role: str) -> bool:
    '''Deterministic: Same user/role → Same decision every time'''
    return user_role in ["admin", "manager"]

# Test: assert grant_access(123, "admin") == True
# Always passes because logic is deterministic
"""
    )


def mlops_era():
    """2015-2021: Data-driven machine learning operations"""
    return ParadigmShift(
        era="MLOps (Code + Data)",
        artifact="Trained model weights, training datasets, feature pipelines",
        determinism="Probabilistic but fixed: Same features → Same model output",
        testing="Cross-validation, confusion matrix, AUC/F1-score thresholds",
        monitoring="Model accuracy, precision/recall, data drift, label drift",
        example="""
def predict_fraud(transaction_amount: float, user_history: List[float]) -> float:
    '''Probabilistic classifier: Learned from training data'''
    features = [transaction_amount, sum(user_history)]
    return fraud_model.predict_proba(features)[1]  # Probability 0.0-1.0

# Test: assert accuracy(predictions, labels) > 0.95
# Depends on training data quality, not just logic
"""
    )


def llmops_era():
    """2023+: Generative AI operations with non-deterministic outputs"""
    return ParadigmShift(
        era="LLMOps (Generative)",
        artifact="Foundation model + prompts + adapters + RAG corpus + guardrails",
        determinism="Non-deterministic: Same prompt → Different output each time",
        testing="Semantic evaluation, hallucination rate, safety screening, LLM-as-Judge",
        monitoring="TTFT/TPOT latency, hallucination rate, token costs, semantic quality",
        example="""
def explain_concept(question: str, temperature: float = 0.7) -> str:
    '''Non-deterministic generation: Multiple valid answers'''
    prompt = f"Explain this clearly: {question}"
    response1 = llm.generate(prompt, temperature=temperature)  # "X is..."
    response2 = llm.generate(prompt, temperature=temperature)  # "X refers to..."
    response3 = llm.generate(prompt, temperature=temperature)  # "The definition..."
    # All three are correct but different

# Test: assert all(semantic_similarity(r, golden) > 0.85 for r in [r1, r2, r3])
# Must account for variability in output
"""
    )


def demonstrate_testing_paradigm_shift():
    """Show how testing evolves across eras"""
    print("\n" + "=" * 70)
    print("TESTING PARADIGM EVOLUTION")
    print("=" * 70)

    test_examples = [
        {
            "era": "DevOps (Deterministic)",
            "assertion": 'assert grant_access(user_id=123, role="admin") == True',
            "behavior": "✓ Always passes (deterministic function)",
        },
        {
            "era": "MLOps (Probabilistic but fixed)",
            "assertion": "assert accuracy(model.predict(X_test), y_test) > 0.95",
            "behavior": "Passes if model is well-trained; depends on data quality",
        },
        {
            "era": "LLMOps (Non-deterministic generation)",
            "assertion": """assert all(
    hallucination_rate(model.generate(prompt, temp=0.7)) < 0.05
    and semantic_similarity(output, golden_response) > 0.85
    for _ in range(5)
)""",
            "behavior": "Requires multiple runs, semantic evaluation, probabilistic metrics",
        }
    ]

    for test in test_examples:
        print(f"\n{test['era']}")
        print(f"  Assertion:\n    {test['assertion']}")
        print(f"  Behavior: {test['behavior']}")


def demonstrate_deployment_shift():
    """Show how deployment strategies evolve"""
    print("\n" + "=" * 70)
    print("DEPLOYMENT STRATEGY EVOLUTION")
    print("=" * 70)

    strategies = {
        "DevOps": {
            "artifact": "Docker image (binary)",
            "validation": "Smoke tests (must pass 100%)",
            "deployment": "Blue-green or rolling (replace deterministic binary)",
            "rollback": "Instant (revert to previous container)",
        },
        "MLOps": {
            "artifact": "Model weights + features pipeline",
            "validation": "Holdout test set (accuracy > threshold)",
            "deployment": "Shadow mode (run in parallel, compare results)",
            "rollback": "Revert model version (features pipeline stays same)",
        },
        "LLMOps": {
            "artifact": "Model + prompts + adapters + safety config",
            "validation": "Canary (10% traffic, monitor hallucination rate)",
            "deployment": "Gradual rollout (10% → 50% → 100% over hours)",
            "rollback": "Automatic (detect regression, revert all components)",
        },
    }

    for strategy, details in strategies.items():
        print(f"\n{strategy}:")
        for key, value in details.items():
            print(f"  {key}: {value}")


def demonstrate_determinism_spectrum():
    """Visualize where different systems fall on the determinism spectrum"""
    print("\n" + "=" * 70)
    print("DETERMINISM SPECTRUM")
    print("=" * 70)

    systems = [
        ("If-then rule", "if age > 18: grant_access()", 100),
        ("Mathematical function", "return 2 * x + 3", 100),
        ("Database query", "SELECT * FROM users WHERE id=123", 100),
        ("Traditional ML classifier", "rf.predict_proba(features)", 95),
        ("Time-series forecasting", "prophet.forecast(periods=30)", 85),
        ("Embeddings + similarity search", "get_top_k_similar(query)", 75),
        ("LLM with prompt engineering", "llm.generate(prompt)", 20),
        ("LLM generation (temp=1.0)", "llm.generate(prompt, temp=1.0)", 5),
    ]

    print("\nSystem Type                          Determinism %")
    print("─" * 70)
    for system, example, determinism in systems:
        bar = "█" * (determinism // 5) + "░" * ((100 - determinism) // 5)
        print(f"{system:<35} {bar} {determinism}%")
        print(f"  {example}")


def demonstrate_monitoring_shift():
    """Show what gets monitored across eras"""
    print("\n" + "=" * 70)
    print("MONITORING METRICS EVOLUTION")
    print("=" * 70)

    monitoring = {
        "DevOps (Code)": [
            "Uptime (99.9%)",
            "Latency (p95 < 100ms)",
            "Error rate (< 0.1%)",
            "CPU/Memory utilization",
        ],
        "MLOps (Code + Data)": [
            "Accuracy / Precision / Recall",
            "Model drift (vs golden metrics)",
            "Data drift (vs baseline distribution)",
            "Prediction latency",
            "Prediction volume",
        ],
        "LLMOps (Generative)": [
            "TTFT (Time-to-First-Token) < 350ms",
            "TPOT (Time-Per-Output-Token) < 30ms",
            "KV cache saturation < 85%",
            "Hallucination rate < 3%",
            "Token costs ($)",
            "Semantic quality (similarity to golden)",
            "Safety scores (jailbreak probability)",
            "User feedback (thumbs-up/-down)",
        ],
    }

    for era, metrics in monitoring.items():
        print(f"\n{era}:")
        for i, metric in enumerate(metrics, 1):
            print(f"  {i}. {metric}")


def main():
    """Run all demonstrations"""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "  MODULE 01: PARADIGM SHIFT - DevOps → MLOps → LLMOps  ".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "═" * 68 + "╝")

    # Display the three paradigms
    print(devops_era())
    print(mlops_era())
    print(llmops_era())

    # Show testing evolution
    demonstrate_testing_paradigm_shift()

    # Show deployment evolution
    demonstrate_deployment_shift()

    # Show determinism spectrum
    demonstrate_determinism_spectrum()

    # Show monitoring evolution
    demonstrate_monitoring_shift()

    print("\n" + "=" * 70)
    print("KEY INSIGHT: LLMOps Challenges")
    print("=" * 70)
    print("""
The fundamental challenge of LLMOps is that outputs are:

1. NON-DETERMINISTIC: Same prompt → Different output each time
2. VARIABLE-LENGTH: Output is 50 words, 500 words, or 5000 words
3. SEMANTICALLY EVALUATED: Cannot use Boolean assertions; must measure quality
4. PROBABILISTICALLY SAMPLED: Temperature, top-p, top-k change behavior

This requires a complete rethinking of:
  • Testing (semantic evaluation instead of assertions)
  • Deployment (canary rollouts instead of instant switches)
  • Monitoring (semantic metrics instead of just latency)
  • Guardrails (multi-tier safety layers)
  • Versioning (prompt + model + adapter versions together)
""")

    print("\n" + "=" * 70)
    print("✓ Paradigm shift demonstration complete")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
