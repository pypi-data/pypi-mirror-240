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
    name = 'nsb_ml_py_pkg',
    version = version,
    author = 'Khandoker Nosiba Arifin',
    author_email = 'nosiba.stu2018@juniv.edu',
    url = 'https://github.com/nosiba28/My-First-ML-Project',
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