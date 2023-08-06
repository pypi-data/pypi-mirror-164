from setuptools import setup, find_packages

setup(name='CGTasks',
      version='1.1.4',
      packages=find_packages(exclude=['CGTasks.tests']),
      install_requires = [
        'MarkLib',
        'CGLib'
      ],
      zip_safe=False)