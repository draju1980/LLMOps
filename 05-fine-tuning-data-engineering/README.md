# Fine-Tuning Data Engineering

**ChatML, Alpaca, Llama-3 formatting; instruction structuring; loss masking (labels=-100 on prompts)**

## Learning Objectives

By the end of this module, you will be able to:

  1. Format instruction data in ChatML/Alpaca/Llama-3
  2. Implement loss masking (train only on responses)
  3. Structure prompt-input-output triples
  4. Validate output format correctness

## Duration

3 hours

## Key Concepts & Topics

  • ChatML format with role markers
  • Alpaca format (instruction/input/output)
  • Llama-3 header format
  • Loss masking implementation (labels=-100)
  • Token validation and edge cases

## Hands-On Labs

  (None)

## Module Structure

```
05-fine-tuning-data-engineering/
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
cd 05-fine-tuning-data-engineering

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

- Source: PDF source-outline.md (Chapter 05)
- Glossary: Module 18
- Interview Prep: Module 17

---

**Last Updated:** 2026-11-05
**Status:** Template (full implementation pending)
