# Module 01: What is LLMOps? - Step-by-Step Instructions

## Overview
This module teaches the **fundamental shift from DevOps → MLOps → LLMOps** and the **9 core pillars** of production LLM systems.

**Time to complete:** 2-3 hours
**Prerequisites:** None - this is the foundation module

---

## What You'll Learn

✓ **Paradigm Shift:** Understand why LLMs are fundamentally different from traditional software  
✓ **9 Pillars:** Learn the complete framework for production-grade LLM systems  
✓ **Non-Deterministic Challenge:** Recognize why testing LLMs is harder than testing code  
✓ **Architecture Differences:** See how LLMOps differs from DevOps and MLOps  

---

## How to Complete This Module

### Step 1: Read the Conceptual Foundation (30 minutes)

Read `README.md` in this directory, which covers:

1. **Learning Objectives** (5 min)
   - What you're trying to accomplish

2. **Course Structure Overview** (10 min)
   - Visual timeline: DevOps → MLOps → LLMOps
   - Core focus areas for each era

3. **Key Concepts** (15 min)
   - 1.1: The Paradigm Shift
   - 1.2: Fundamental Architectural Difference
   - Understand the non-deterministic nature of LLMs

**Expected outcome:** You can explain why `llm.generate()` is different from `if age > 18:`

---

### Step 2: Study the 9 Pillars (45 minutes)

In `README.md`, read section **"The Nine Core Pillars of LLMOps"**

For each pillar, understand:
- **What:** What does this pillar do?
- **Why:** Why does it matter for production?
- **Technologies:** What tools implement it?
- **Example:** Concrete example of the pillar in action

**Pillars:**
1. Data Preparation & Curation
2. Experimentation & Model Selection
3. Prompt Management & Versioning
4. Fine-Tuning & Adaptation
5. High-Throughput Deployment & Serving
6. Continuous Monitoring & Observability
7. Safety, Moderation & Responsible AI
8. Workflow Orchestration
9. Automation & Continuous Alignment

**Expected outcome:** You can describe all 9 pillars and why they're needed

---

### Step 3: Complete Exercise 1.1 (30 minutes)

**File:** `exercises/exercise_1_1.py`

**What to do:**
```bash
cd 01-what-is-llmops
python3 exercises/exercise_1_1.py
```

**Exercise:** Identify which pillars, testing strategies, and risks apply to:
1. **Payment Service** (deterministic)
2. **Fraud Detector ML** (probabilistic but fixed)
3. **Customer Support Chatbot** (non-deterministic generation)

**What you'll learn:**
- How to map real-world systems to LLMOps frameworks
- Why different systems need different testing approaches
- How to spot production risks early

**Expected output:**
```
✓ Paradigm Shift Identification - Complete analysis of all 3 systems
✓ Key Insights - Understanding of determinism spectrum
✓ Risk surfaces - What can go wrong in production
✓ Deployment strategies - How to safely roll out each system
```

---

### Step 4: Complete Exercise 1.2 (45 minutes)

**File:** `exercises/exercise_1_2.py`

**What to do:**
```bash
cd 01-what-is-llmops
python3 exercises/exercise_1_2.py
```

**Exercise:** Assess a **Financial Advisor Chatbot** against all 9 pillars:
- Is each pillar implemented? (Yes/Partial/No)
- Is it production-grade?
- What are the gaps?
- What's the priority to fix it?

**What you'll learn:**
- How to audit existing LLM applications
- How to build a roadmap for production readiness
- How to prioritize what to build first

**Expected output:**
```
✓ Detailed assessment of each pillar
✓ Summary scorecard (e.g., 2/9 pillars production-grade = 20% ready)
✓ Prioritized roadmap (High/Medium/Low)
✓ Actionable mitigation strategies for 90-day plan
✓ Key takeaways about common mistakes
```

---

## Validation Checklist

After completing this module, you should be able to answer:

- [ ] **What's the fundamental difference between DevOps and LLMOps?**  
  *Answer: DevOps handles deterministic code; LLMOps handles non-deterministic generation*

- [ ] **Name all 9 pillars of LLMOps**  
  *Answer: Can list all 9 + brief description of each*

- [ ] **Why can't you test an LLM with simple assertions like `assert output == "expected"`?**  
  *Answer: LLMs generate non-deterministic outputs; must test semantic properties instead*

- [ ] **What pillars are missing from a basic Flask + GPT-3.5 chatbot?**  
  *Answer: Recognize that most startups skip 7 of 9 pillars*

- [ ] **How would you prioritize fixing a production LLM system that's only 20% ready?**  
  *Answer: Start with High priority pillars (data, safety, observability)*

---

## What's Next?

After completing this module:

1. **Module 02:** Learn the 7-stage LLMOps lifecycle
2. **Module 03:** Scalable data preparation with DuckDB
3. **Modules 04-19:** Deep dive into each pillar

---

## Quick Reference

### Key Terms
- **TTFT:** Time-to-First-Token (prefill latency)
- **TPOT:** Time-Per-Output-Token (decoding latency)
- **LoRA:** Low-Rank Adaptation (parameter-efficient fine-tuning)
- **RAG:** Retrieval-Augmented Generation (fact augmentation)
- **Hallucination:** Model inventing false information
- **Non-deterministic:** Output varies probabilistically

### Key Files in This Module
- `README.md` - Comprehensive conceptual guide
- `exercises/exercise_1_1.py` - Paradigm shift identification
- `exercises/exercise_1_2.py` - 9 pillars assessment
- `src/01_paradigm_shift.py` - Code examples
- `src/02_nine_pillars.py` - Pillar deep dive
- `tests/test_module_01.py` - Validation tests

---

## Troubleshooting

**Q: I don't understand the difference between deterministic and non-deterministic**  
A: Run both exercises. Exercise 1.1 explains this with concrete examples.

**Q: The 9 pillars seem overwhelming - do I need all of them?**  
A: Yes, but implement them in priority order. Start with data quality and safety first.

**Q: How do I know if my LLM system is production-ready?**  
A: Use Exercise 1.2's assessment framework. Aim for 80%+ pillar readiness.

---

## Run Tests

To verify you understand the material:

```bash
cd 01-what-is-llmops
make test          # Run unit tests
make validate      # Validate your understanding
make lab           # Run both exercises
```

**Expected outcome:** All tests pass ✓

---

**Last Updated:** 2026-11-06  
**Status:** Complete  
**Difficulty:** Beginner (Foundations)
