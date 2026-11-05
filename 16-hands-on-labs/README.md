# Hands-On Labs & Implementation Exercises

**Complete Lab 1, 2, 3 with automated graders and full solutions**

## Learning Objectives

By the end of this module, you will be able to:

  1. Complete Lab 1: VRAM budgeting with solutions
  2. Complete Lab 2: Canary deployment with rollback
  3. Complete Lab 3: Prompt template skew detection
  4. Pass all automated graders

## Duration

6 hours

## Key Concepts & Topics

  • Lab 1: VRAM calculator (Module 08)
  • Lab 2: Canary rollout script (Module 10)
  • Lab 3: Prompt skew detector (Module 11)
  • Automated test harnesses
  • Solutions and explanations

## Hands-On Labs

  • Lab 1
  • Lab 2
  • Lab 3

## Module Structure

```
16-hands-on-labs/
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
cd 16-hands-on-labs

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

- Source: PDF source-outline.md (Chapter 16)
- Glossary: Module 18
- Interview Prep: Module 17

---

**Last Updated:** 2026-11-05
**Status:** Template (full implementation pending)
