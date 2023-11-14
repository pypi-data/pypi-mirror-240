from setuptools import setup, find_packages

setup(
    name='maskingPackage',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'pandas',  # Add any dependencies here
        'os',
        'csv',
        'cryptography'
    ],
)
