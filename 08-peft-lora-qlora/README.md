# PEFT: LoRA & QLoRA

**Parameter-efficient fine-tuning: LoRA mathematics, CPU-friendly training, VRAM budgeting**

## Learning Objectives

By the end of this module, you will be able to:

  1. Understand LoRA mathematics (W = W₀ + (α/r)(B×A))
  2. Train LoRA on CPU-friendly model (SmolLM2-135M)
  3. Calculate VRAM budgets for QLLoRA
  4. Complete Lab 1: VRAM Sizing Exercise

## Duration

5 hours

## Key Concepts & Topics

  • LoRA mathematics and decomposition
  • QLoRA 4-bit quantization (NF4, double quantization)
  • CPU training (SmolLM2-135M default)
  • GPU training (14B+ models with QLoRA)
  • VRAM calculator: base + adapters + optimizer + KV cache

## Hands-On Labs

  • Lab 1: VRAM Budgeting & QLLoRA Sizing Calculation

## Module Structure

```
08-peft-lora-qlora/
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
cd 08-peft-lora-qlora

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

- Source: PDF source-outline.md (Chapter 08)
- Glossary: Module 18
- Interview Prep: Module 17

---

**Last Updated:** 2026-11-05
**Status:** Template (full implementation pending)
