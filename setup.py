import os
import subprocess

import setuptools
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from setuptools.command.install import install


# Base class for setting environment variables
class SetEnvCommand:
    def set_environment(self):
        print("Setting SETUPTOOLS_USE_DISTUTILS=local")
        os.environ["SETUPTOOLS_USE_DISTUTILS"] = "local"


# Custom install command
class CustomInstallCommand(install, SetEnvCommand):
    def run(self):
        self.set_environment()
        # Run parent install
        install.run(self)


# Custom develop command
class CustomDevelopCommand(develop, SetEnvCommand):
    def run(self):
        self.set_environment()
        develop.run(self)


# Custom egg_info command
class CustomEggInfoCommand(egg_info, SetEnvCommand):
    def run(self):
        self.set_environment()
        egg_info.run(self)


setuptools.setup(
    py_modules=[],
    cmdclass={
        "install": CustomInstallCommand,
        "develop": CustomDevelopCommand,
        "egg_info": CustomEggInfoCommand,
    },
)
