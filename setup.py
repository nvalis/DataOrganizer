'''Setup file for installing with package control.'''
import setuptools


with open('README.md') as file:
    LONG_DESCRIPTION = file.read()

setuptools.setup(
    name='DataOrganizer',
    version='0.1',
    author='Nvalis',
    description='Data organization tool for e.g. measurement data.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/nvalis/DataOrganizer',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],)
