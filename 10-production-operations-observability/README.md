# Production Operations & Observability

**Golden Signals (TTFT, TPOT, KV cache, perplexity), OpenTelemetry, Prometheus, Grafana**

## Learning Objectives

By the end of this module, you will be able to:

  1. Implement Golden Signals metrics collection
  2. Setup OpenTelemetry instrumentation
  3. Create Prometheus/Grafana dashboards
  4. Complete Lab 2: Canary Rollout & Automated Rollback

## Duration

4 hours

## Key Concepts & Topics

  • Golden Signals: TTFT, TPOT, KV cache saturation, perplexity
  • Semantic quality metrics (hallucination rate, similarity)
  • OpenTelemetry instrumentation and spans
  • Prometheus metrics scraping
  • Grafana dashboard setup
  • Lab 2: Canary deployment with automated rollback

## Hands-On Labs

  • Lab 2: End-to-End Canary Rollout & Automated Rollback Script

## Module Structure

```
10-production-operations-observability/
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
cd 10-production-operations-observability

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

- Source: PDF source-outline.md (Chapter 10)
- Glossary: Module 18
- Interview Prep: Module 17

---

**Last Updated:** 2026-11-05
**Status:** Template (full implementation pending)
