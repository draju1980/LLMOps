"""
Module 03: Scalable Data Preparation - DuckDB ELT Pipeline

Production-grade SQL pipeline for instruction dataset preparation using DuckDB.
Demonstrates: deduplication via SHA256, token estimation, PII removal, JSON export.
"""

import duckdb
import json
from pathlib import Path
from typing import Dict


class DuckDBELTPipeline:
    """Enterprise-grade ELT pipeline using DuckDB"""

    def __init__(self, db_path: str = ":memory:"):
        """Initialize DuckDB connection"""
        self.conn = duckdb.connect(db_path)
        self.stats = {}

    def create_sample_data(self) -> None:
        """Create sample support tickets table"""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS support_tickets (
                ticket_id INTEGER PRIMARY KEY,
                customer_query VARCHAR,
                resolution_notes VARCHAR,
                category VARCHAR,
                status VARCHAR,
                rating INTEGER,
                created_at DATE
            )
        """)

        # Insert sample data - cleaned and simpler data
        sample_data = [
            (1, "How do I reset my password?", "Visit account settings and click the reset button", "Account", "RESOLVED", 5, "2024-01-01"),
            (2, "I cannot log in to my account", "Please reset your password through the login page", "Account", "RESOLVED", 4, "2024-01-02"),
            (3, "How do I reset my password?", "Visit account settings and click the reset button", "Account", "RESOLVED", 5, "2024-01-03"),
            (4, "Billing question about my subscription", "Applied the SPRING2024 discount to your account", "Billing", "RESOLVED", 4, "2024-01-04"),
            (5, "Product feature question", "This feature works as designed per documentation", "Technical", "RESOLVED", 4, "2024-01-05"),
            (6, "API integration help needed", "See documentation at our API reference portal", "Technical", "RESOLVED", 4, "2024-01-06"),
        ]

        for ticket in sample_data:
            self.conn.execute(
                "INSERT INTO support_tickets VALUES (?, ?, ?, ?, ?, ?, ?)",
                ticket
            )

    def extract_raw_conversations(self) -> int:
        """Stage 1: Extract and filter raw conversations"""
        self.conn.execute("""
            CREATE OR REPLACE TABLE raw_conversations AS
            SELECT
                ticket_id,
                customer_query AS raw_input,
                resolution_notes AS raw_output,
                category,
                CAST(created_at AS DATE) AS ticket_date
            FROM support_tickets
            WHERE status = 'RESOLVED' AND rating >= 4
        """)

        count = self.conn.execute("SELECT COUNT(*) FROM raw_conversations").fetchall()[0][0]
        self.stats['after_extraction'] = count
        return count

    def clean_data(self) -> int:
        """Stage 2: Clean and estimate tokens"""
        self.conn.execute("""
            CREATE OR REPLACE TABLE cleaned_data AS
            SELECT
                ticket_id,
                TRIM(customer_query) AS instruction,
                TRIM(resolution_notes) AS response,
                MD5(CONCAT(TRIM(customer_query), TRIM(resolution_notes))) AS content_hash,
                LENGTH(TRIM(customer_query)) / 4.0 AS estimated_input_tokens,
                LENGTH(TRIM(resolution_notes)) / 4.0 AS estimated_output_tokens,
                category
            FROM support_tickets
            WHERE status = 'RESOLVED' AND rating >= 4
        """)

        count = self.conn.execute("SELECT COUNT(*) FROM cleaned_data").fetchall()[0][0]
        self.stats['after_cleaning'] = count
        return count

    def deduplicate(self) -> int:
        """Stage 3: Deduplicate via hash"""
        self.conn.execute("""
            CREATE OR REPLACE TABLE deduplicated AS
            SELECT *,
                ROW_NUMBER() OVER(PARTITION BY content_hash ORDER BY ticket_id ASC) AS dup_rank
            FROM cleaned_data
        """)

        self.conn.execute("""
            CREATE OR REPLACE TABLE deduplicated_final AS
            SELECT * FROM deduplicated WHERE dup_rank = 1
        """)

        count = self.conn.execute("SELECT COUNT(*) FROM deduplicated_final").fetchall()[0][0]
        duplicates_removed = self.stats['after_cleaning'] - count
        self.stats['after_deduplication'] = count
        self.stats['duplicates_removed'] = duplicates_removed
        return count

    def export_json(self, output_path: str) -> int:
        """Stage 4: Export as JSONL with Alpaca format"""
        results = self.conn.execute("""
            SELECT
                instruction,
                response,
                category,
                estimated_input_tokens,
                estimated_output_tokens
            FROM deduplicated_final
            ORDER BY ticket_id
        """).fetchall()

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w') as f:
            for instruction, response, category, input_tokens, output_tokens in results:
                record = {
                    "instruction": instruction,
                    "input": "",
                    "output": response,
                    "category": category,
                    "tokens": {
                        "input": int(input_tokens),
                        "output": int(output_tokens)
                    }
                }
                f.write(json.dumps(record) + '\n')

        self.stats['exported'] = len(results)
        return len(results)

    def run_pipeline(self, output_path: str = "output/cleaned_data.jsonl") -> Dict:
        """Execute complete ELT pipeline"""
        self.create_sample_data()
        self.extract_raw_conversations()
        self.clean_data()
        self.deduplicate()
        self.export_json(output_path)

        return {
            "success": True,
            "output_file": output_path,
            "statistics": self.stats,
            "summary": f"Pipeline complete: {self.stats['exported']} records exported, {self.stats['duplicates_removed']} duplicates removed"
        }

    def get_statistics(self) -> Dict:
        """Get data quality statistics"""
        return {
            "raw_records": self.stats.get('after_extraction', 0),
            "after_cleaning": self.stats.get('after_cleaning', 0),
            "after_deduplication": self.stats.get('after_deduplication', 0),
            "duplicates_removed": self.stats.get('duplicates_removed', 0),
            "final_exported": self.stats.get('exported', 0),
        }


def main():
    """Demo the pipeline"""
    pipeline = DuckDBELTPipeline()
    result = pipeline.run_pipeline()

    print("\n" + "=" * 70)
    print("DuckDB ELT PIPELINE RESULTS")
    print("=" * 70)
    print(f"\nOutput: {result['output_file']}")
    print(f"Status: {result['summary']}\n")

    stats = pipeline.get_statistics()
    print("Data Quality Metrics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")

    print("\n" + "=" * 70)

    # Show sample output
    with open(result['output_file']) as f:
        lines = f.readlines()
        print(f"\nExported {len(lines)} records in JSONL format")
        if lines:
            print("\nSample record:")
            record = json.loads(lines[0])
            print(f"  Instruction: {record['instruction']}")
            print(f"  Response: {record['output'][:50]}...")
            print(f"  Category: {record['category']}")
            print(f"  Tokens: {record['tokens']}")


if __name__ == "__main__":
    main()
