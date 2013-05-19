from setuptools import setup, find_packages
import sys
import os

version = '0.1.0a1'

setup(name='txScheduler',
      version=version,
      description="Twisted extension for scheduling tasks",
      long_description="""\
""",
      classifiers=['License :: OSI Approved :: MIT License'], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Kevin Horn',
      author_email='kevin.horn@gmail.com',
      url='',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'python-dateutil>=1.1'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
