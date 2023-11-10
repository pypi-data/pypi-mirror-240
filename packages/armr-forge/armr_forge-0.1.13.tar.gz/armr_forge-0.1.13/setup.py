# setup.py
from setuptools import setup, find_packages

setup(
    name='armr_forge',
    version='0.1.13',
    packages=['armr_forge'],
    install_requires=[
	'bcrypt>=4.0.1',
	'cryptography>=41.0.5',
	'numpy>=1.26.1',
	'pandas>=2.1.2',
    ],
    # Metadata
    author='StalwartBI',
    license='Apache License 2.0, BSD 3-Clause License',
    author_email='StalwartBI@outlook.com',
    description='A fully encrypted secure ETL data collection library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/StalwartBI/armr_forge/armr_forge",

)