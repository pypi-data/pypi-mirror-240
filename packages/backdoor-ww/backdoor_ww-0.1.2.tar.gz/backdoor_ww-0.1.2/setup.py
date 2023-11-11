from setuptools import setup
from setuptools import find_packages


VERSION = '0.1.2'


setup(
    name='backdoor_ww',  # package name
    version=VERSION,  # package version
    description='Backdoor attack by PyPI package',  # package description
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={"backdoor_ww":["*.txt"]},
    script=['script.py'],
    zip_safe=False,
)
