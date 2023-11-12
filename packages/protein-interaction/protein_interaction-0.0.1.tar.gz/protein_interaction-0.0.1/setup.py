from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='protein_interaction',
    packages=find_packages(include=["protein_interaction"]),
    version='0.0.1',
    description='Library for getting interactions of proteins',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Shiva Aryal',
)