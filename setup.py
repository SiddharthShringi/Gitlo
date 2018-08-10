from setuptools import setup
import setuptools

setup(
    name='pygit',
    version='1.0',
    url="https://github.com/SiddharthShringi/Gitpy",
    author="Siddharth Shringi",
    author_email="siddharthshrigi@gmail.com",
    description="A Command Line Interface for accessing Github api.",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    py_modules=['pygit'],
    install_requires=[
        'Click', 'Requests',
    ],
    entry_points='''
        [console_scripts]
        pygit=pygit:cli
    ''',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ),
)
