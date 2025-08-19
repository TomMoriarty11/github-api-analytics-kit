import pytest
from github_api_analytics_kit.utils.aggregator import aggregate_commits_by_week

def test_aggregate_commits_by_week():
    sample_data = [
        {"commit": {"author": {"date": "2025-08-12T14:23:00Z"}}},
        {"commit": {"author": {"date": "2025-08-13T09:47:00Z"}}}
    ]
    result = aggregate_commits_by_week(sample_data)
    assert not result.empty
    assert "commit_count" in result.columns
