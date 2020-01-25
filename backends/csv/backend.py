from backend import Backend, ParsingError
from metadata import MetaData

import re


class CSVBackend(Backend):
    def __init__(self, data_file_path, comments='#'):
        super().__init__(data_file_path)
        self._begin_re = re.compile(f'^{comments} ?BEGINMETA$')
        self._parameter_re = re.compile(f'{comments} ?(?P<parameter>.+): ?(?P<value>.*)$')
        self._end_re = re.compile(f'{comments} ?ENDMETA$')
        self.meta_data = self.parse()

    def parse(self):
        meta_data = self._read_meta_block()
        md = MetaData(self.data_file_path)
        for parameter, value in meta_data.items():
            md.set_parameter(parameter, value)
        return md

    def _read_meta_block(self):
        meta_data = {}
        with open(self.data_file_path) as data_file:
            line = ''
            while not self._begin_re.match(line):
                line = data_file.readline()

            while True:
                line = data_file.readline()
                match = self._parameter_re.match(line)
                if not match:
                    if self._end_re.match(line):
                        break
                    else:
                        raise ParsingError(f'Could not find parameter and value in \'{line}\'')
                meta_data[match.group('parameter')] = match.group('value')

        return meta_data