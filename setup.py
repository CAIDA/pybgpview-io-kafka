#!/usr/bin/env python
#

from setuptools import setup, find_packages

setup(name='pybgpview.io.kafka',
      version='0.1',
      description='BGPView Kafka IO module',
      url='https://github.com/CAIDA/pybgpview-io-kafka',
      author='Alistair King',
      author_email='alistair@caida.org',
      license='BSD',
      packages=find_packages(),
      entry_points={'console_scripts': [
          'bgpview-server-kafka=pybgpview.io.kafka.server:main'
      ]},
      install_requires=['pykafka', 'python-snappy', 'pytimeseries'])
