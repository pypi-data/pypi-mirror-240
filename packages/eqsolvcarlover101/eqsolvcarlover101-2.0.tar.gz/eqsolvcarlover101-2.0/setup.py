from setuptools import setup
from pathlib import Path


directory = Path("eqsolve/README.md").parent
long_description = (directory / "README.md").read_text()

setup(
    name="eqsolvcarlover101",
    package_data={
        "eqsolve": ['README.md'],
        "eqsolve": ['LICENSE'],
    },
    include_package_data=True,
    version="2.0",
    author="Zakkai Thomas",
    author_email="zmanmustang2017@gmail.com",
    description="Automatic equation solver   -|-   Use import eqsolve",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Carlover101/equation-solver",
    packages=["eqsolve/equation", "eqsolve/other", "eqsolve"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    password="Mowermania@2020",
)
