# Kubeflow Pipelines (KFP v2)

**Containerized DAGs with typed components: Extract→Tokenize→Train→Evaluate→Deploy gate**

## Learning Objectives

By the end of this module, you will be able to:

  1. Build KFP v2 pipelines with @dsl.component
  2. Define strongly-typed inputs/outputs
  3. Create conditional deployment gates
  4. Execute locally without Kubernetes

## Duration

4 hours

## Key Concepts & Topics

  • KFP v2 pipeline definition
  • @dsl.component decorators
  • Typed inputs/outputs
  • Conditional branching (dsl.If)
  • Local Docker runner (no Kubernetes required)

## Hands-On Labs

  (None)

## Module Structure

```
06-kubeflow-pipelines/
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
cd 06-kubeflow-pipelines

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

- Source: PDF source-outline.md (Chapter 06)
- Glossary: Module 18
- Interview Prep: Module 17

---

**Last Updated:** 2026-11-05
**Status:** Template (full implementation pending)
