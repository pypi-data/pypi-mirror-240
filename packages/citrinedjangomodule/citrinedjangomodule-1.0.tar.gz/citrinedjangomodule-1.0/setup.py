
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='citrinedjangomodule',
    version='1.0',
    packages=['university'],
    install_requires=requirements,
    author='Farah Ben Mohamed',
    author_email='farahbenmohamed.carnelian@gmail.com',
    description='citrinedjangomodule',
)
