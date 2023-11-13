from setuptools import setup, find_packages

setup(
    name='ctx-timer',
    version='0.1.0',
    packages=find_packages(),
    description='A simple context manager for timing code execution',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='João Gabriel Lima',
    author_email='joaogabriellima.eng@gmail.com',
    url='https://github.com/jgabriellima/ctx-timer',
    install_requires=[],
    classifiers=[],
)
