"""
Module 03 Exercise 3.1: Extend the DuckDB ELT Pipeline

Task: Add token filtering to the pipeline.

Requirements:
1. Add a filtering stage that removes records with < 5 input tokens or > 500 output tokens
2. Implement a method called `filter_by_token_count()`
3. Create a statistics method showing how many records were filtered
4. Update the pipeline to call this filter stage

Expected Output:
- Pipeline should report records filtered by token count
- Statistics should track filtered records separately from duplicates
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from duckdb_elt_pipeline import DuckDBELTPipeline


class ExtendedDuckDBELTPipeline(DuckDBELTPipeline):
    """Extended pipeline with token filtering"""

    def filter_by_token_count(self, min_input: int = 5, max_output: int = 500) -> int:
        """Filter records by token count"""
        self.conn.execute(f"""
            CREATE OR REPLACE TABLE token_filtered AS
            SELECT *
            FROM deduplicated_final
            WHERE estimated_input_tokens >= {min_input}
            AND estimated_output_tokens <= {max_output}
        """)

        count = self.conn.execute("SELECT COUNT(*) FROM token_filtered").fetchall()[0][0]
        before = self.conn.execute("SELECT COUNT(*) FROM deduplicated_final").fetchall()[0][0]
        filtered_out = before - count

        self.stats['after_token_filter'] = count
        self.stats['token_filtered_out'] = filtered_out

        return count

    def run_extended_pipeline(self, output_path: str = "output/extended_output.jsonl") -> dict:
        """Run pipeline with token filtering"""
        self.create_sample_data()
        self.extract_raw_conversations()
        self.clean_data()
        self.deduplicate()
        self.filter_by_token_count()

        # Export from filtered dataset
        results = self.conn.execute("""
            SELECT instruction, response, category,
                   estimated_input_tokens, estimated_output_tokens
            FROM token_filtered ORDER BY ticket_id
        """).fetchall()

        import json
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

        return {
            "success": True,
            "output_file": output_path,
            "statistics": self.stats,
        }


def main():
    """Run the extended pipeline"""
    pipeline = ExtendedDuckDBELTPipeline()
    result = pipeline.run_extended_pipeline()

    print("\n" + "=" * 70)
    print("EXTENDED DuckDB ELT PIPELINE WITH TOKEN FILTERING")
    print("=" * 70)
    print(f"\nOutput: {result['output_file']}")

    stats = result['statistics']
    print(f"\nPipeline Statistics:")
    print(f"  Raw records: {stats.get('after_extraction', 0)}")
    print(f"  After cleaning: {stats.get('after_cleaning', 0)}")
    print(f"  After deduplication: {stats.get('after_deduplication', 0)}")
    print(f"  Duplicates removed: {stats.get('duplicates_removed', 0)}")
    print(f"  After token filtering: {stats.get('after_token_filter', 0)}")
    print(f"  Token-filtered out: {stats.get('token_filtered_out', 0)}")
    print(f"  Final exported: {stats.get('exported', 0)}")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
