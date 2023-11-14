from setuptools import setup, find_packages

setup(
    name='maskingPackage',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'pandas',  # Add any dependencies here
        'json',
        'os',
        'csv',
        'cryptography'
    ],
)
