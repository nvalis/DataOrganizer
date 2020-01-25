class MetaData:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self.parameters = {}

    def __repr__(self):
    	return f'<{self.__class__.__name__}: {self.data_file_path} ({len(self.parameters)} parameters)>'

    def add_parameter(self, parameter):
        self.parameters[parameter] = None

    def set_parameter(self, parameter, value):
        self.parameters[parameter] = value

    def get_parameter(self, parameter):
        return self.parameters[parameter]
