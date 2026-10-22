from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="foss-fincalc",
    version="1.0.0",
    author="ananthicoder-debug",
    author_email="ananthigomathi202006@gmail.com",
    description="Open Source Financial and Loan Analytics Package for FOSS Course 19CSP01",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ananthicoder-debug/foss-assignment2-custom-package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "foss-fincalc=foss_fincalc.cli:main",
        ],
    },
)
