from setuptools import setup

setup(
    name='gitpy',
    version='0.1',
    py_modules=['gitpy'],
    install_requires=[
        'Click', 'Requests',
    ],
    entry_points='''
        [console_scripts]
        gitpy=gitpy:cli
    ''',
)
