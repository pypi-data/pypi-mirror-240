from setuptools import setup, find_packages
import os

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

def read_file(file):
   with open(file, encoding='utf-8') as f:
        return f.read()
    
long_description = read_file(os.path.abspath("README.md"))
version = "1.0.2"
requirements = read_requirements(os.path.abspath("requirements.txt"))

setup(
    name = 'my_first_py_pkg',
    version = version,
    author = 'Md. Masum Bhuiyan',
    author_email = 'masumbhuiyan577@gmail.com',
    url = 'https://github.com/BhuiyanMasum/...',
    description = 'My first python package',
    long_description_content_type = "text/markdown",
    long_description = long_description,
    license = "MIT license",
    packages = find_packages(exclude=["test"]),
    install_requires = requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)