"""This is the setup for the pyinterpolation package"""

from setuptools import setup

setup(
    name='markovanalysis',
    version="1.0",
    license='Simplified BSD License',
    setup_requires=['numpy>=1.7.1'],
    tests_require=['numpy>=1.7.1', 'nose>=1.3'],
    install_requires=['numpy>=1.7.1'],
    packages=['markovanalysis'],
    test_suite='nose.collector')
