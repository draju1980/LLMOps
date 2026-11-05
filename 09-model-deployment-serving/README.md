# Model Deployment & High-Throughput Serving

**FastAPI + vLLM async streaming: PagedAttention, continuous batching, SamplingParams**

## Learning Objectives

By the end of this module, you will be able to:

  1. Build async FastAPI server with streaming
  2. Use vLLM's PagedAttention and continuous batching
  3. Implement Server-Sent Events (SSE) streaming
  4. Achieve TTFT < 350ms and TPOT < 30ms

## Duration

4 hours

## Key Concepts & Topics

  • Anti-pattern: Naive Flask wrapper (why it fails)
  • Production: FastAPI + vLLM async engine
  • PagedAttention (KV cache as fixed-size blocks)
  • Continuous batching (iterate-level scheduling)
  • Streaming via Server-Sent Events (SSE)
  • SamplingParams (temperature, top-p, max_tokens)

## Hands-On Labs

  (None)

## Module Structure

```
09-model-deployment-serving/
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
cd 09-model-deployment-serving

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

- Source: PDF source-outline.md (Chapter 09)
- Glossary: Module 18
- Interview Prep: Module 17

---

**Last Updated:** 2026-11-05
**Status:** Template (full implementation pending)
