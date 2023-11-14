from os import path
from setuptools import setup, find_packages

with open(path.join("..", 'README.md'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    author="Teddy Tortorici",
    description="Tools to assist in angle tuning grazing incidence x-ray scattering (GIWAXS or GISASXS) experiments",
    long_description="README.md",
    name="gixtpy",
    version='0.1.0',
    packages=find_packages(include=['gixtpy.*']),
    install_requires=[
         "numpy",
        "scipy",
        "matplotlib",
        "tk",
        "tifffile",
        "jupyter",
    ],
    python_requires=">=3.8"
)
