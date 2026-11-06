"""
Exercise 1.2: 9 Pillars Mapping

Task: Map an LLM application to the 9 pillars. For each pillar, answer:
1. Do we have it? (Yes/No/Partial)
2. Is it production-grade?
3. If not, what's the gap?

This exercise uses an example application: Financial Advisor Chatbot
"""

from typing import Dict, List


class PillarAssessment:
    """Assessment of a pillar's implementation status"""

    def __init__(
        self,
        name: str,
        status: str,  # "Yes", "Partial", "No"
        is_production_grade: bool,
        gaps: List[str] = None,
        priority: str = "High",  # High, Medium, Low
    ):
        self.name = name
        self.status = status
        self.is_production_grade = is_production_grade
        self.gaps = gaps or []
        self.priority = priority

    def __str__(self):
        status_emoji = {
            "Yes": "✓",
            "Partial": "◐",
            "No": "✗",
        }[self.status]

        prod_emoji = "✓" if self.is_production_grade else "⚠️"
        priority_emoji = {
            "High": "🔴",
            "Medium": "🟡",
            "Low": "🟢",
        }[self.priority]

        result = f"\n{self.name}\n"
        result += f"  Status: {status_emoji} {self.status}\n"
        result += f"  Production-Grade: {prod_emoji}\n"
        result += f"  Priority: {priority_emoji} {self.priority}\n"

        if self.gaps:
            result += "  Gaps:\n"
            for gap in self.gaps:
                result += f"    • {gap}\n"

        return result


def example_financial_advisor_assessment() -> Dict[str, PillarAssessment]:
    """
    Example: Financial Advisor Chatbot Assessment

    A startup built a chatbot using GPT-3.5 that gives investment advice.
    Currently, it's deployed on a simple Flask server with no monitoring.
    """

    return {
        "pillar_1": PillarAssessment(
            name="Pillar 1: Data Preparation & Curation",
            status="Partial",
            is_production_grade=False,
            gaps=[
                "Using raw Wikipedia + Reddit posts (not cleaned or deduplicated)",
                "No PII removal (financial records might be exposed)",
                "Token length validation missing",
                "No versioning of training datasets",
            ],
            priority="High",
        ),
        "pillar_2": PillarAssessment(
            name="Pillar 2: Experimentation & Model Selection",
            status="No",
            is_production_grade=False,
            gaps=[
                "Currently only using GPT-3.5 (via OpenAI API)",
                "No comparison with open models (Llama, Mistral)",
                "No cost/latency/accuracy trade-off analysis",
                "Can't switch models without rewriting code",
            ],
            priority="High",
        ),
        "pillar_3": PillarAssessment(
            name="Pillar 3: Prompt Management & Versioning",
            status="Partial",
            is_production_grade=False,
            gaps=[
                "Prompts hardcoded in Python files (no version control)",
                "System prompt: 'You are a financial advisor' (too generic)",
                "No Jinja2 templating (can't inject variables)",
                "No automated linting for missing variables",
                "Train-serve skew risk: Training used different prompt",
            ],
            priority="High",
        ),
        "pillar_4": PillarAssessment(
            name="Pillar 4: Fine-Tuning & Adaptation",
            status="No",
            is_production_grade=False,
            gaps=[
                "No fine-tuning (using base GPT-3.5)",
                "Can't teach custom domain vocabulary (tax terms, regulations)",
                "No adapter weights versioning",
                "Not using LoRA or other parameter-efficient methods",
            ],
            priority="Medium",
        ),
        "pillar_5": PillarAssessment(
            name="Pillar 5: High-Throughput Deployment & Serving",
            status="No",
            is_production_grade=False,
            gaps=[
                "Naive Flask endpoint (synchronous)",
                "No streaming (client waits for full response)",
                "External API dependency (OpenAI latency)",
                "No load balancing or autoscaling",
                "No health checks or graceful degradation",
            ],
            priority="High",
        ),
        "pillar_6": PillarAssessment(
            name="Pillar 6: Continuous Monitoring & Observability",
            status="No",
            is_production_grade=False,
            gaps=[
                "No Prometheus/Grafana setup",
                "No latency tracking (TTFT, TPOT)",
                "No semantic quality metrics (hallucination rate)",
                "OpenAI API cost unknown (no tracking)",
                "User complaints only noticed via support tickets",
            ],
            priority="High",
        ),
        "pillar_7": PillarAssessment(
            name="Pillar 7: Safety, Moderation & Responsible AI",
            status="No",
            is_production_grade=False,
            gaps=[
                "No prompt injection detection",
                "No PII scrubbing on user inputs",
                "No hallucination detection (model might invent stock prices!)",
                "No jailbreak protection",
                "Not flagging dangerous financial advice (e.g., 'all-in crypto')",
            ],
            priority="High",
        ),
        "pillar_8": PillarAssessment(
            name="Pillar 8: Workflow Orchestration",
            status="No",
            is_production_grade=False,
            gaps=[
                "No automated training pipeline",
                "No retraining schedule",
                "Manual updates (run script locally, push)",
                "No regression testing before deployment",
                "Can't rollback quickly if something breaks",
            ],
            priority="Medium",
        ),
        "pillar_9": PillarAssessment(
            name="Pillar 9: Automation & Continuous Alignment",
            status="No",
            is_production_grade=False,
            gaps=[
                "Manual deployments via git push + ssh",
                "No deployment gates (quality checks)",
                "No canary routing (all-or-nothing deployments)",
                "No automatic rollback on failure",
                "User feedback not collected or used",
            ],
            priority="Medium",
        ),
    }


def print_assessment(assessment: Dict[str, PillarAssessment]):
    """Pretty-print assessment"""

    print("\n" + "=" * 80)
    print("EXERCISE 1.2: 9 PILLARS MAPPING - EXAMPLE SOLUTION")
    print("=" * 80)
    print("\nApplication: Financial Advisor Chatbot (GPT-3.5 via API)")
    print("Current State: Deployed but not production-ready")
    print("\n" + "=" * 80)

    # Print all assessments
    assessments_dict = assessment
    for pillar_key, pillar_assessment in assessments_dict.items():
        print(pillar_assessment)

    # Calculate scores
    total = len(assessments_dict)
    fully_implemented = sum(1 for a in assessments_dict.values() if a.status == "Yes")
    partially_implemented = sum(1 for a in assessments_dict.values() if a.status == "Partial")
    not_implemented = sum(1 for a in assessments_dict.values() if a.status == "No")
    production_grade = sum(1 for a in assessments_dict.values() if a.is_production_grade)

    print("\n" + "=" * 80)
    print("SUMMARY SCORECARD")
    print("=" * 80)
    print(f"\nTotal Pillars: {total}")
    print(f"  Fully Implemented: {fully_implemented} ✓")
    print(f"  Partially Implemented: {partially_implemented} ◐")
    print(f"  Not Implemented: {not_implemented} ✗")
    print(f"\nProduction-Grade Pillars: {production_grade}/{total}")
    print(f"Readiness Score: {(production_grade / total * 100):.0f}%")


def print_priority_roadmap(assessment: Dict[str, PillarAssessment]):
    """Print prioritized implementation roadmap"""

    print("\n" + "=" * 80)
    print("PRIORITIZED IMPLEMENTATION ROADMAP")
    print("=" * 80)

    by_priority = {
        "High": [],
        "Medium": [],
        "Low": [],
    }

    for pillar_key, assessment in assessment.items():
        by_priority[assessment.priority].append(assessment.name)

    print("\n🔴 HIGH PRIORITY (Implement First - Blocks Deployment)")
    for item in by_priority["High"]:
        print(f"  1. {item}")

    print("\n🟡 MEDIUM PRIORITY (Implement Next - Improves Reliability)")
    for item in by_priority["Medium"]:
        print(f"  2. {item}")

    print("\n🟢 LOW PRIORITY (Nice-to-Have - Optimization)")
    for item in by_priority["Low"]:
        print(f"  3. {item}")


def print_gap_mitigation_strategies(assessment: Dict[str, PillarAssessment]):
    """Print actionable mitigation strategies"""

    print("\n" + "=" * 80)
    print("MITIGATION STRATEGIES (Next 90 Days)")
    print("=" * 80)

    strategies = {
        "Pillar 1": "Use SEC filings + news for clean data. Implement SHA256 hashing.",
        "Pillar 2": "Benchmark GPT-3.5 vs Llama 2 70B on finance Q&A. Track cost/latency.",
        "Pillar 3": "Move prompts to git-versioned Jinja2 files. Add linting.",
        "Pillar 5": "Use vLLM for streaming. Reduce latency from 2s to <500ms.",
        "Pillar 6": "Setup Prometheus/Grafana. Track TTFT, hallucination rate, cost.",
        "Pillar 7": "Add safety classifier for financial advice (e.g., flag >50% portfolio in 1 stock).",
        "Pillar 8": "Build KFP pipeline: Extract Q&As → Fine-tune → Benchmark → Deploy.",
        "Pillar 9": "GitHub Actions: Deploy on merge. Canary 10% traffic first.",
    }

    for pillar, strategy in strategies.items():
        print(f"\n{pillar}:")
        print(f"  → {strategy}")


def main():
    """Run the exercise"""
    assessment = example_financial_advisor_assessment()

    print_assessment(assessment)
    print_priority_roadmap(assessment)
    print_gap_mitigation_strategies(assessment)

    print("\n" + "=" * 80)
    print("KEY TAKEAWAY")
    print("=" * 80)
    print("""
This Financial Advisor Chatbot is currently at ~20% production readiness.

The founder's common mistakes:
  1. Skipped data curation (used raw web data)
  2. No model selection (locked into OpenAI)
  3. Hardcoded prompts (no versioning)
  4. No safety guardrails (could give dangerous advice)
  5. No monitoring (finding issues via user complaints)
  6. Manual deployments (slow, error-prone)

To reach production readiness (80%+):
  → Focus on HIGH priority pillars first (data, serving, safety, observability)
  → Budget 90 days for implementation
  → Allocate 2–3 engineers full-time
  → Use the roadmap above to track progress
""")

    print("\n" + "=" * 80)
    print("✓ Exercise 1.2 complete")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
