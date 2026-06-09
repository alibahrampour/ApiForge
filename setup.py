from setuptools import setup, find_packages

setup(
    name="apiforge",
    version="0.2.0",
    author="Ali Bahrampour",
    author_email="alibahrampour.76@gmail.com",
    description="API Testing Platform for generating, executing and analyzing API test scenarios.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alibahrampour/apiforge",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "flask>=3.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Testing",
        "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords=[
        "api",
        "testing",
        "curl",
        "postman",
        "qa",
        "automation",
        "api-testing",
        "rest-api",
        "postman-collection"
    ],
)