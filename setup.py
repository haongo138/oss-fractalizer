from setuptools import setup

setup(
    name='fractalizer',
    version='0.1.0',
    author='Hao Ngo',
    author_email='hyosimple@gmail.com',
    description='Generate and display various fractals',
    packages=['src'],
    install_requires=[
        'numpy',
        'matplotlib',
    ],
)