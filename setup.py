from setuptools import setup
import setuptools

setup(
    name='gitpy',
    version='1.0',
    url="https://github.com/SiddharthShringi/Gitpy",
    autor="Siddharth Shringi",
    autor_email="siddharthshrigi@gmail.com",
    description="A Command Line Interface for accessing Github api.",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    py_modules=['gitpy'],
    install_requires=[
        'Click', 'Requests',
    ],
    entry_points='''
        [console_scripts]
        gitpy=gitpy:cli
    ''',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
