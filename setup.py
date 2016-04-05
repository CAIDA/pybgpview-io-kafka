#!/usr/bin/env python
#

from setuptools import setup

setup(name='pybgpview',
      version='0.1',
      description='BGPView Kafka IO module',
      url='https://github.com/CAIDA/bgpview-io-kafka',
      author='Alistair King',
      author_email='alistair@caida.org',
      license='BSD',
      packages=['pybgpview'],
      entry_points={'console_scripts': [
          'bgpview-server-kafka=pybgpview.io.kafka.server:main'
      ]},
      install_requires=['pykafka', 'python-snappy'])
