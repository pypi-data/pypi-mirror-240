from setuptools import setup, find_packages


setup (
    author= "Julio César Martínez",
    description="A package to simulate stochastic proccesses",
    name='stochasticmodels',
    version='0.1.0',
    packages=find_packages(include=["numpy", "pandas", ""]),
    ),


# pip install -e .