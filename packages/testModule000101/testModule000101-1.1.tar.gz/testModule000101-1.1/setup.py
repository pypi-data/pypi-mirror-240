
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='testModule000101',
    version='1.1',
    packages=['myapp'],
    install_requires=requirements,
    author='Farah Ben Mohamed',
    author_email='farahbenmohamed.carnelian@gmail.com',
    description='testModule00010',
)
#username : farahCarnelian / password : Py2023_test*