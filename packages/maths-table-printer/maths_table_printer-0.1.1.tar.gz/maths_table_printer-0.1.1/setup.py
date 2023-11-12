from setuptools import setup, find_packages

setup(
    name='maths_table_printer',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'maths_table_printer = maths_table_printer.printer:main',
        ],
    },
    include_package_data=True,
)
