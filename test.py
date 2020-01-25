#!/usr/bin/env python3
from DataOrganizer.backends import CSVBackend


def csv_test():
    csv_file = 'DataOrganizer/backends/csv/testdata/file1.csv'
    parser = CSVBackend(csv_file)
    print(parser)
    print(parser.meta_data)
    print(parser.meta_data.parameters)


if __name__ == '__main__':
    csv_test()
