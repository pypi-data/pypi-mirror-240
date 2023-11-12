# setup.py
from setuptools import setup, find_packages

with open('long_description.md', 'r', encoding='utf-8') as file:
    long_description = file.read()
    
setup(
    name='fastapi-logger',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'fastapi',
    ],
    author='untitled69.ipynb',
    author_email='ravis2114@gmail.com',
    description='FastAPI Logger: Enhance your FastAPI applications with comprehensive request logging.',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
