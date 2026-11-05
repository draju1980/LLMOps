"""
Exercise 1.1: Paradigm Shift Identification

Scenario: Your company has three systems:
1. Payment service (deterministic)
2. Fraud detector ML model (probabilistic but fixed)
3. Customer support chatbot (non-deterministic generation)

Task: For each system, identify:
- Which pillar(s) of LLMOps it needs
- What testing strategy is appropriate
- What could go wrong in production
"""

from typing import Dict, List, Tuple


def analyze_system(
    name: str,
    description: str,
    paradigm: str,
) -> Dict:
    """Analyze a system across paradigm categories"""

    analysis = {
        "Payment Service": {
            "paradigm": "DevOps (Deterministic)",
            "pillars_needed": ["None (DevOps only)"],
            "testing_strategy": [
                "Unit tests: assert compute_charge(100) == 15.00",
                "Edge cases: assert compute_charge(0.01) == 0.00",
                "Integration: assert payment processor receives exact amount",
            ],
            "production_risks": [
                "Floating-point rounding errors (rare but catastrophic)",
                "Currency conversion precision",
                "Payment processor timeouts",
            ],
            "why": "Deterministic logic; testing is straightforward assertions",
        },
        "Fraud Detector": {
            "paradigm": "MLOps (Probabilistic but fixed)",
            "pillars_needed": [
                "Pillar 2: Model Selection (benchmark models)",
                "Pillar 6: Observability (precision/recall monitoring)",
                "Pillar 8: Orchestration (retraining pipeline)",
                "Pillar 9: Automation (deployment gates on metrics)",
            ],
            "testing_strategy": [
                "Confusion matrix: TP, FP, TN, FN",
                "Precision > 0.95 (false positives hurt customer experience)",
                "Recall > 0.85 (miss real fraud)",
                "ROC curve and AUC-ROC",
                "Cross-validation on historical data",
            ],
            "production_risks": [
                "Model drift: fraudsters evolve tactics",
                "Label drift: fraud definition changes",
                "Threshold miscalibration: FP vs FN trade-off",
                "Class imbalance: fraud is rare (0.1% of transactions)",
            ],
            "why": (
                "Output is fixed (given trained model) but depends on training data. "
                "Testing is probabilistic: threshold-based metrics."
            ),
        },
        "Customer Support Chatbot": {
            "paradigm": "LLMOps (Non-deterministic generation)",
            "pillars_needed": [
                "Pillar 1: Data Prep (clean Q&A pairs)",
                "Pillar 2: Model Selection (OpenAI vs Llama vs Mistral)",
                "Pillar 3: Prompt Management (version templates)",
                "Pillar 4: Fine-Tuning (adapt tone to brand voice)",
                "Pillar 5: Serving (vLLM for latency)",
                "Pillar 6: Observability (hallucination rate, user satisfaction)",
                "Pillar 7: Safety (jailbreak detection, data leakage)",
                "Pillar 8: Orchestration (retraining on user feedback)",
                "Pillar 9: Automation (canary deployment, A/B testing)",
            ],
            "testing_strategy": [
                "Multiple generations per prompt (3–5 runs)",
                "Semantic similarity to golden response > 0.85",
                "Hallucination rate < 3% (LLM-as-Judge)",
                "Safety scoring (jailbreak probability < 1%)",
                "Fact-checking against knowledge base",
                "User satisfaction surveys",
            ],
            "production_risks": [
                "Hallucination: Model invents false product specs",
                "Jailbreaks: User tricks model into ignoring guardrails",
                "Inconsistency: Same question → Different answers (confusing)",
                "Data leakage: Model regurgitates confidential internal docs",
                "Tone drift: Sounds robotic or sarcastic",
                "Token costs: $100K/month if not optimized",
            ],
            "why": (
                "Non-deterministic generation requires semantic testing. "
                "Multiple production concerns: quality, safety, cost, consistency."
            ),
        },
    }

    return analysis.get(name, {})


def print_analysis():
    """Print detailed analysis for all three systems"""

    print("\n" + "=" * 80)
    print("EXERCISE 1.1: PARADIGM SHIFT IDENTIFICATION - SOLUTION")
    print("=" * 80)

    systems = [
        "Payment Service",
        "Fraud Detector",
        "Customer Support Chatbot",
    ]

    for system_name in systems:
        analysis = analyze_system(system_name, "", "")

        print(f"\n{'─' * 80}")
        print(f"SYSTEM: {system_name}")
        print(f"{'─' * 80}")

        print(f"\nParadigm: {analysis['paradigm']}")

        print(f"\nLLMOps Pillars Needed:")
        for pillar in analysis["pillars_needed"]:
            print(f"  • {pillar}")

        print(f"\nTesting Strategy:")
        for test in analysis["testing_strategy"]:
            print(f"  • {test}")

        print(f"\nProduction Risks:")
        for risk in analysis["production_risks"]:
            print(f"  ⚠️  {risk}")

        print(f"\nWhy This Paradigm:")
        print(f"  {analysis['why']}")


def key_insights():
    """Print key insights from the exercise"""

    print("\n" + "=" * 80)
    print("KEY INSIGHTS")
    print("=" * 80)
    print("""
1. DETERMINISM SPECTRUM
   Payment Service is fully deterministic (100% reproducible)
   → Testing: Boolean assertions, exact equality

   Fraud Detector is probabilistic but FIXED (given trained model)
   → Testing: Statistical metrics (precision, recall, AUC)

   Chatbot is non-deterministic GENERATION (inherent variability)
   → Testing: Semantic evaluation, probabilistic metrics

2. PILLAR COMPLEXITY
   Payment Service: 0 LLMOps pillars (pure DevOps)
   Fraud Detector: 4 pillars (data quality, model selection, observability)
   Chatbot: All 9 pillars required (full LLMOps stack)

3. RISK SURFACES
   Payment: Technical (rounding errors, timeouts)
   Fraud Detector: Statistical (drift, calibration)
   Chatbot: Semantic (hallucination, jailbreaks, tone)

4. TESTING PARADIGM
   Payment: 1 run sufficient (deterministic)
   Fraud Detector: Cross-validation on full dataset
   Chatbot: Multiple runs with semantic evaluation

5. DEPLOYMENT STRATEGY
   Payment: Instant blue-green (binary switch safe)
   Fraud Detector: Shadow mode (compare predictions)
   Chatbot: Canary rollout (10% traffic, monitor quality)
""")


if __name__ == "__main__":
    print_analysis()
    key_insights()

    print("\n" + "=" * 80)
    print("✓ Exercise 1.1 complete")
    print("=" * 80 + "\n")
