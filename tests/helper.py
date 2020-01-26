"""Helper functions for the unit tests."""
import os.path


def get_path(filename):
    """
    Get the absolute name of the test file to be independent from where the tests are executed.

    Args:
        filename (str): filename of the file to get from the release_configurations folder.
    """
    abs_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(abs_path, 'csv', filename)
