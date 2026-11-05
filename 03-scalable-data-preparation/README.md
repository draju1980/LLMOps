# Module 03: Scalable Data Preparation

**Production DuckDB ELT Pipeline for Instruction Dataset Preparation**

## Learning Objectives

By the end of this module, you will be able to:

  1. Understand in-warehouse ELT philosophy vs memory-bound Pandas
  2. Write production SQL pipelines in DuckDB for data cleaning
  3. Implement automated deduplication via content hashing
  4. Estimate token counts and validate data quality
  5. Export clean instruction datasets in Alpaca JSON format

## Duration

3-4 hours

## Implementation Details

### Files

- **`src/duckdb_elt_pipeline.py`** (200 lines): Main pipeline with 4 stages
  - Stage 1: Extract raw conversations (filter by status & rating)
  - Stage 2: Clean data (trim, hash, estimate tokens)
  - Stage 3: Deduplicate (via MD5 hash, keep first occurrence)
  - Stage 4: Export as Alpaca JSONL format

- **`tests/test_elt_pipeline.py`** (120 lines): 7 unit tests (all passing ✅)
  - Extract, clean, deduplicate, export, end-to-end, PII filtering tests

- **`exercises/exercise_3_1.py`** (100 lines): Extend pipeline with token filtering
  - Add `filter_by_token_count()` method
  - Track filtering statistics
  - Export filtered results

### 4-Stage ELT Pipeline

**Stage 1: Extract Raw Conversations**
```sql
SELECT ticket_id, customer_query AS raw_input, resolution_notes AS raw_output
FROM support_tickets
WHERE status = 'RESOLVED' AND rating >= 4
```
Result: 6 records from sample data

**Stage 2: Clean Data**
```sql
SELECT
  ticket_id,
  TRIM(customer_query) AS instruction,
  TRIM(resolution_notes) AS response,
  MD5(...) AS content_hash,
  LENGTH(...) / 4.0 AS estimated_input_tokens,
  LENGTH(...) / 4.0 AS estimated_output_tokens
```
Result: 6 cleaned records

**Stage 3: Deduplicate**
```sql
WITH deduplicated AS (
  SELECT *,
    ROW_NUMBER() OVER(PARTITION BY content_hash ORDER BY ticket_id) AS dup_rank
  FROM cleaned_data
)
SELECT * FROM deduplicated WHERE dup_rank = 1
```
Result: 5 records (1 duplicate removed)

**Stage 4: Export Alpaca Format**
```json
{"instruction": "...", "input": "", "output": "...", "category": "...", "tokens": {"input": 6, "output": 12}}
```
Result: `output/cleaned_data.jsonl` with 5 records

## Key Concepts & Topics

  • **ELT Philosophy**: Push computation to warehouse, not local Pandas
  • **In-Warehouse Processing**: DuckDB (or BigQuery/Snowflake) handles heavy lifting
  • **Content-Based Deduplication**: MD5/SHA256 hashes enable strict matching
  • **Token Estimation**: Length / 4.0 heuristic (1 token ≈ 4 characters)
  • **Data Quality Metrics**: Track at each stage (extraction, cleaning, deduplication)
  • **Structured Export**: JSON Lines with validated schema

## Tests

All 7 tests passing:

```bash
$ cd 03-scalable-data-preparation
$ python3 -m pytest tests/test_elt_pipeline.py -v
```

Output:
```
tests/test_elt_pipeline.py::TestELTPipeline::test_extract_raw_conversations PASSED
tests/test_elt_pipeline.py::TestELTPipeline::test_clean_data PASSED
tests/test_elt_pipeline.py::TestELTPipeline::test_deduplicate PASSED
tests/test_elt_pipeline.py::TestELTPipeline::test_export_json PASSED
tests/test_elt_pipeline.py::TestELTPipeline::test_complete_pipeline PASSED
tests/test_elt_pipeline.py::TestELTPipeline::test_pii_filtering PASSED
tests/test_elt_pipeline.py::test_pipeline_demo PASSED
============================== 7 passed in 0.09s ===============================
```

## Running the Pipeline

```bash
# Install dependencies
pip install -r requirements.txt

# Run the main pipeline
python3 src/duckdb_elt_pipeline.py

# Output:
# ======================================================================
# DuckDB ELT PIPELINE RESULTS
# ======================================================================
# Output: output/cleaned_data.jsonl
# Status: Pipeline complete: 5 records exported, 1 duplicates removed
#
# Data Quality Metrics:
#   raw_records: 6
#   after_cleaning: 6
#   after_deduplication: 5
#   duplicates_removed: 1
#   final_exported: 5

# Run all tests
python3 -m pytest tests/test_elt_pipeline.py -v

# Run an exercise (token filtering)
python3 exercises/exercise_3_1.py
```

## Module Structure

```
03-scalable-data-preparation/
├── README.md                              # This file
├── Makefile                               # Standard targets
├── docker-compose.yml                     # (Minimal for this module)
├── requirements.txt                       # duckdb, pydantic
├── src/
│   └── duckdb_elt_pipeline.py             # Main 4-stage pipeline (200 lines)
├── exercises/
│   └── exercise_3_1.py                    # Token filtering extension (100 lines)
├── solutions/
│   └── exercise_3_1_solution.md           # Solution walkthrough
├── tests/
│   └── test_elt_pipeline.py               # 7 unit tests (all passing ✅)
└── data/
    └── .gitkeep
```

## Quick Start

```bash
cd 03-scalable-data-preparation

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python3 src/duckdb_elt_pipeline.py

# Run all tests
make test

# Run an exercise
python3 exercises/exercise_3_1.py

# View exported data
cat output/cleaned_data.jsonl | head -1 | python3 -m json.tool
```

## Key Takeaways

1. **ELT > ETL for LLMs**: Push processing to the warehouse (DuckDB, BigQuery), not Pandas
2. **Window Functions**: Use ROW_NUMBER() for efficient deduplication
3. **Content Hashing**: MD5/SHA256 enables strict deduplication without storing full text
4. **Token Estimation**: Essential for cost/budget planning
5. **Data Quality Tracking**: Every stage should report metrics
6. **Structured Export**: Alpaca format validation for downstream processing

## Production Considerations

- **Scalability**: DuckDB can handle billions of rows with minimal memory
- **Idempotency**: Pipeline is idempotent (safe to rerun)
- **Observability**: Track metrics at each stage
- **Extensibility**: Easy to add custom filters/validation

## Next Steps

- ✅ Understand ELT vs ETL philosophy
- ✅ Implement basic SQL pipeline
- ✅ Test deduplication and token estimation
- → Module 04: Dataset Engineering & Lineage (versioning, lineage DAGs)
- → Module 05: Fine-Tuning Data Engineering (ChatML formatting)

## References

- **Source**: PDF source-outline.md (Chapter 3: Scalable Data Preparation)
- **Technology**: DuckDB 1.0.0, Pydantic 2.5
- **Format**: Alpaca instruction tuning
- **Related**: Module 04 (lineage), Module 05 (formatting)

---

**Last Updated:** 2026-11-05  
**Status:** ✅ Implementation Complete  
**Tests:** 7/7 passing ✅  
**Exercises:** 1/1 complete ✅  
**Learning Time:** 3-4 hours recommended
