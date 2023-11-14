#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from pathlib import Path

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

# Get the path to the requirements.txt file
requirements_path = Path(__file__).parent / 'requirements_dev.txt'

# Read the contents of the requirements file
with open(requirements_path) as f:
    requirements = f.read().splitlines()

test_requirements = [
    "pytest>=3",
]

setup(
    author="Jack Tierney",
    author_email="jackcurragh@gmail.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.10",
    ],
    description="A python command-line utility for the generation of comprehensive reports on the quality of ribosome profiling (Ribo-Seq) datasets",
    entry_points={
        "console_scripts": [
            "RiboMetric=RiboMetric.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    # long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="RiboMetric",
    name="RiboMetric",
    packages=find_packages(
        include=["RiboMetric", "RiboMetric.*"],
        exclude=[
            "sample_data/*",
        ],
    ),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/JackCurragh/RiboMetric",
    version="0.1.9",
    zip_safe=False,
)
