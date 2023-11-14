from setuptools import setup, find_packages

setup(
    name='cyprint',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'cyprint = cyprint:cyprint',
        ],
    },
)
