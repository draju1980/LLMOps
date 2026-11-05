# LLMOps vs LLM System Design

**Demarcation: Infrastructure (ops) vs Application (AI architects), Hybrid RAG with RRF**

## Learning Objectives

By the end of this module, you will be able to:

  1. Distinguish LLMOps from LLM system design
  2. Design hybrid RAG with Reciprocal Rank Fusion
  3. Understand infrastructure vs application concerns
  4. Plan enterprise search architecture

## Duration

2 hours

## Key Concepts & Topics

  • LLMOps: Reliability, automation, latency SLAs
  • System Design: Domain reasoning, RAG, agents
  • Hybrid search: Dense (vector) + Sparse (BM25)
  • Reciprocal Rank Fusion algorithm
  • Cross-Encoder reranking
  • Infrastructure vs Application architecture

## Hands-On Labs

  (None)

## Module Structure

```
14-llmops-vs-llm-system-design/
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
cd 14-llmops-vs-llm-system-design

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

- Source: PDF source-outline.md (Chapter 14)
- Glossary: Module 18
- Interview Prep: Module 17

---

**Last Updated:** 2026-11-05
**Status:** Template (full implementation pending)
