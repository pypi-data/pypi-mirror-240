from setuptools import setup, find_packages

setup(
    name="treat_rl",
    version="0.2.1",
    packages=find_packages(),
    install_requires=[
        "gym",
        "numpy",
        # other dependencies
    ],
)
