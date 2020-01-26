"""
Unit tests for the MetaData class.
"""
from DataOrganizer.metadata import MetaData


def test_metadata():
    """Test creating and modifying a meta-data parameter."""
    meta_data = MetaData('filename.csv')
    meta_data.add_parameter('test')
    meta_data.set_parameter('test', 123)
    assert meta_data.get_parameter('test') == 123
