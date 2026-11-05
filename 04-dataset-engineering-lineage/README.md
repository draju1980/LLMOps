# Dataset Engineering & Lineage

**Cryptographic versioning, immutability, provenance DAGs, train/val/test split leakage prevention**

## Learning Objectives

By the end of this module, you will be able to:

  1. Generate immutable dataset manifests (SHA256)
  2. Track data lineage as DAGs
  3. Prevent train/val/test leakage
  4. Version datasets like code artifacts

## Duration

3 hours

## Key Concepts & Topics

  • Dataset manifest generation (Python script)
  • SHA256 content hashing for immutability
  • Data lineage DAGs
  • Entity-based leakage prevention
  • MLflow artifact registration

## Hands-On Labs

  (None)

## Module Structure

```
04-dataset-engineering-lineage/
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
cd 04-dataset-engineering-lineage

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

- Source: PDF source-outline.md (Chapter 04)
- Glossary: Module 18
- Interview Prep: Module 17

---

**Last Updated:** 2026-11-05
**Status:** Template (full implementation pending)
