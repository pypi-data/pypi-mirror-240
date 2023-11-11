from typing import *
from setuptools import setup, find_packages
import os

setup_file_dir = os.path.dirname(__file__)
python_dir = os.path.dirname(setup_file_dir)
luna_viz_dir = os.path.dirname(python_dir)

requirements_file = os.path.join(luna_viz_dir, "requirements.txt")
assert os.path.isfile(requirements_file)

with open(requirements_file) as f:
    requirements_list : List[str]  = f.read().split("\n")

setup(
    name='luna_viz',
    version='0.0.1',
    packages=["luna_viz"],
    install_requires=requirements_list,
    # Entry points create executable scripts for the user
    entry_points={
        'console_scripts': [
            'tpx3plot = luna_viz.tpx3plot:main',
        ]
    },
)
