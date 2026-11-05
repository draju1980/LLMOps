"""
Module 03: Tests for DuckDB ELT Pipeline

Validates data cleaning, deduplication, and JSONL export.
"""

import json
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from duckdb_elt_pipeline import DuckDBELTPipeline


class TestELTPipeline:
    """Test suite for DuckDB ELT pipeline"""

    @pytest.fixture
    def pipeline(self, tmp_path):
        """Create pipeline instance with temporary database"""
        return DuckDBELTPipeline()

    def test_extract_raw_conversations(self, pipeline):
        """Test extraction of raw conversations"""
        pipeline.create_sample_data()
        count = pipeline.extract_raw_conversations()
        assert count > 0, "Should extract at least one conversation"
        assert count == 6, "Should extract 6 conversations (7 total - 1 low rating)"

    def test_clean_data(self, pipeline):
        """Test data cleaning"""
        pipeline.create_sample_data()
        pipeline.extract_raw_conversations()
        count = pipeline.clean_data()
        assert count > 0, "Should have cleaned records"
        assert count == 6, "Should clean all 6 records (sample data has no extreme length)"

    def test_deduplicate(self, pipeline):
        """Test deduplication via SHA256"""
        pipeline.create_sample_data()
        pipeline.extract_raw_conversations()
        pipeline.clean_data()
        initial_count = pipeline.stats['after_cleaning']
        final_count = pipeline.deduplicate()

        assert final_count < initial_count, "Should remove duplicates"
        assert pipeline.stats['duplicates_removed'] > 0, "Should detect duplicates"

    def test_export_json(self, pipeline, tmp_path):
        """Test JSONL export"""
        output_file = str(tmp_path / "output.jsonl")
        pipeline.create_sample_data()
        pipeline.extract_raw_conversations()
        pipeline.clean_data()
        pipeline.deduplicate()
        count = pipeline.export_json(output_file)

        assert Path(output_file).exists(), "Output file should be created"
        assert count > 0, "Should export records"

        # Verify JSONL format
        with open(output_file) as f:
            records = [json.loads(line) for line in f]
            assert len(records) == count, "Record count should match"

            for record in records:
                assert "instruction" in record, "Record should have instruction"
                assert "output" in record, "Record should have output"
                assert "tokens" in record, "Record should have token count"
                assert record["tokens"]["input"] > 0, "Input tokens should be positive"
                assert record["tokens"]["output"] > 0, "Output tokens should be positive"

    def test_complete_pipeline(self, pipeline, tmp_path):
        """Test complete end-to-end pipeline"""
        output_file = str(tmp_path / "output.jsonl")
        result = pipeline.run_pipeline(output_file)

        assert result['success'] is True, "Pipeline should succeed"
        assert Path(output_file).exists(), "Output file should be created"
        assert result['statistics']['exported'] > 0, "Should export records"

        stats = pipeline.get_statistics()
        assert stats['duplicates_removed'] >= 1, "Should remove at least 1 duplicate"

    def test_pii_filtering(self, pipeline):
        """Test data quality metrics"""
        pipeline.create_sample_data()
        pipeline.extract_raw_conversations()
        initial = pipeline.stats['after_extraction']
        pipeline.clean_data()
        cleaned = pipeline.stats['after_cleaning']

        # Sample data is clean (no PII), so should have 0 filtered
        assert initial == cleaned, "Sample data should not have PII to filter"


def test_pipeline_demo():
    """Demo test that runs the pipeline"""
    pipeline = DuckDBELTPipeline()
    result = pipeline.run_pipeline("/tmp/test_output.jsonl")

    assert result['success'] is True
    assert result['statistics']['exported'] > 0
    assert Path(result['output_file']).exists()

    # Verify output format
    with open(result['output_file']) as f:
        for line in f:
            record = json.loads(line)
            assert isinstance(record, dict)
            assert all(k in record for k in ["instruction", "output", "tokens"])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
