from setuptools import setup, find_packages

setup(
    name="apiforge",
    version="0.1.0",
    description="Generate CURL commands and Postman collections from API scenarios",
    author="Ali Bahrampour",
    packages=find_packages(),
    python_requires=">=3.10",
)