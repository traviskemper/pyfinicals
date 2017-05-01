#!/usr/bin/env python

#Afrom distutils.core import setup
from setuptools import setup

#  packages=['streamm', 'streamm.jobs', 'streamm.jobs', 'streamm.mpi', 'streamm.simulation', 'streamm.structure'],
# dep = ['os','sys','shutil','time','datetime','json','math','numpy','copy','scipy','random','json','optparse','logging','pickle']
#  dep openbabel ( py27-openbabel )

setup(name='mortgage',
      version='0.1',
      url='http://traviskemper.com',
      author='Travis W. Kemper ',
      author_email='travis.kemper.w@gmail.com',
      py_modules=['mortgage'],
      # test_suite = 'tests',
      # data_files=['streamm/periodic_table.json']
      )
