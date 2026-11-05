# Prompt Management & Train-Serve Skew

**Centralized Prompt Registry, Jinja2 templates, automated linting, zero-skew detection**

## Learning Objectives

By the end of this module, you will be able to:

  1. Manage prompts in centralized Jinja2 registry
  2. Implement Pydantic v2 validation
  3. Detect and prevent train-serve skew
  4. Complete Lab 3: Prompt Template Skew Detection

## Duration

3 hours

## Key Concepts & Topics

  • Centralized Prompt Registry (Postgres-backed)
  • Jinja2 templating with required variables
  • Pydantic v2 contract validation
  • Automated linting (check for missing variables)
  • Zero-skew detector (byte-for-byte tokenizer match)
  • Lab 3: Prompt template CI test

## Hands-On Labs

  • Lab 3: Prompt Template Skew Detection Test Suite

## Module Structure

```
11-prompt-management-train-serve-skew/
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
cd 11-prompt-management-train-serve-skew

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

- Source: PDF source-outline.md (Chapter 11)
- Glossary: Module 18
- Interview Prep: Module 17

---

**Last Updated:** 2026-11-05
**Status:** Template (full implementation pending)
