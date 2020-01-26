"""
Unit tests for the CSV backend.
"""
import pytest
from DataOrganizer.backends import CSVBackend
from DataOrganizer.backend import ParsingError
from .helper import get_path


def test_correct_file():
    """Check a correctly formatted file."""
    meta_data = CSVBackend(get_path('file_working.csv')).meta_data
    assert meta_data.get_parameter('alpha') == '42.1337'
    assert meta_data.get_parameter('beta') == 'lorem ipsum'


def test_wrong_file():
    """Check if error is thrown if meta-data line is malformed."""
    with pytest.raises(ParsingError):
        CSVBackend(get_path('file_malformed.csv'))
