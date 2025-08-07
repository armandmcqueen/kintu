"""Pytest configuration and shared fixtures."""

import pytest


@pytest.fixture
def sample_config():
    """Provide a sample configuration for testing."""
    return {
        "api_key": "test-key",
        "model": "test-model",
        "temperature": 0.7,
    }
