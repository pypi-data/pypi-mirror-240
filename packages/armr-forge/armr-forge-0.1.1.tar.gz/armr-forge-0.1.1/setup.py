# setup.py
from setuptools import setup, find_packages

setup(
    name='armr-forge',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
	'bcrypt>=4.0.1',
	'cryptography>=41.0.5',
	'numpy>=1.26.1',
	'pandas>=2.1.2',
    ],
    # Metadata
    author='StalwartBI',
    license='Apache License 2.0,BSD 3-Clause License',
    author_email='StalwartBI@outlook.com',
    description='A fully encrypted secure ETL data collection library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

)