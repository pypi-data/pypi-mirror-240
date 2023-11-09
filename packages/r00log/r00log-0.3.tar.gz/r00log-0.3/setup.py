from setuptools import setup, find_packages
import os

script_path = os.path.abspath(__file__)
directory_path = os.path.dirname(script_path)
directory_name = os.path.basename(directory_path)

setup(
    name=directory_name,
    version='0.3',
    packages=find_packages(),
)
