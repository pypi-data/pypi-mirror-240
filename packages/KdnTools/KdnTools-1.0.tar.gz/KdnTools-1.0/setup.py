from setuptools import setup, find_packages

setup(
    name='KdnTools',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'prettytable',
        'colorama',
        'keyboard',
    ],
)
