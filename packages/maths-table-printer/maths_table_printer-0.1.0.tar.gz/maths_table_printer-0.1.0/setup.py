# maths_table_printer/setup.py
from setuptools import setup, find_packages

setup(
    name='maths_table_printer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'maths_table_printer = maths_table_printer.printer:main',
        ],
    },
)