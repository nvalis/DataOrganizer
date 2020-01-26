"""Meta data storage."""


class MetaData:
    """Class to store and manipulate MetaData.

    Args:
        data_file_path (str): Path to the data file.
    """
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self.parameters = {}

    def __repr__(self):
        return (f'<{self.__class__.__name__}: {self.data_file_path}'
                f' ({len(self.parameters)} parameters)>')

    def add_parameter(self, parameter):
        """Add a new parameter to the meta data.

        Args:
            parameter (str): Name of the parameter.
        """
        self.parameters[parameter] = None

    def set_parameter(self, parameter, value):
        """Set the value of a parameter.

        Args:
            parameter (str): Name of the parameter.
            value: New value.
        """
        self.parameters[parameter] = value

    def get_parameter(self, parameter):
        """Get the value of a parameter.

        Args:
            parameter (str): Name of the parameter.
        Returns:
            Value of the parameter.
        """
        return self.parameters[parameter]
