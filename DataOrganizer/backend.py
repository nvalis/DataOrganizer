from .metadata import MetaData


class ParsingError(Exception):
    def __init__(self, msg=''):
        self.msg = msg
    def __repr__(self):
        return f'{self.__class__.__name__}: {self.msg}' 


class Backend:
    """General backend for parsing data files for meta data."""

    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self.meta_data = None

    def parse(self):
        """Parse meta data parameters and values from data file."""

        raise NotImplementedError

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.data_file_path}>'
