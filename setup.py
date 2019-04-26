from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='megaLib',
    version='0.9.5',
    py_modules=['megalib'],
    install_requires=['requests'],
    url='https://github.com/jvdspeare/megaLib',
    license='GPLv3',
    author='james.speare',
    author_email='info.megalib@gmail.com',
    description='megaLib is a Python wrapper for the Megaport RESTful API',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
