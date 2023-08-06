from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="timenet2300", # Replace with your own username
    version="0.0.1",
    author="timenet2300",
    author_email="timenet2300@gmail.com",
    description="Create A small package to work with prime numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/clement-bonnet/medium-first-package",
    url="https://github.com/myNKUST/myprimelib9.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)