from setuptools import setup, find_packages
import sys
sys.path[0:0] = ['src/gscrud']


setup(
    name='lkmongodbprovider',
    version='0.1',
    description='LavKode MongoDB provider',
    long_description='LavKode MongoDB provider',
    author='muthugit',
    author_email='base.muthupandian@gmail.com',
    url='https://muthupandian.in',
    packages=['lkmongoprovider'],
    install_requires=[
        "lkinterface>=0.3",
    ]
)
