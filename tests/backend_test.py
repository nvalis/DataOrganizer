"""
Unit tests for the base backend.
"""
import pytest
from DataOrganizer.backend import Backend


def test_not_implemented():
    """Check if base backend gives NotImplementedError."""
    with pytest.raises(NotImplementedError):
        backend = Backend('filename.csv')
        backend.parse()
