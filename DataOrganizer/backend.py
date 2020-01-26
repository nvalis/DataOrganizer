"""Default backend."""


class ParsingError(Exception):
    """Error for parsing problems.

    Args:
        msg (str): Error message.
    """
    def __init__(self, msg=''):
        super().__init__()
        self.msg = msg

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.msg}'


class Backend:
    """General backend for parsing data files for meta data.

    Args:
        data_file_path (str): Path to the data file.
    """

    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self.meta_data = None

    def parse(self):
        """Parse meta data parameters and values from data file."""
        raise NotImplementedError

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.data_file_path}>'
