from setuptools import setup, find_packages

setup(name='CGTasks',
      version='1.1.3',
      description='',
      url='https://github.com/OGKG/CGTasks',
      author='Vsevolod Hermaniuk',
      author_email='shermanyuk@knu.ua',
      license='MIT',
      packages=find_packages(),
      install_requires = [
        'MarkLib',
        'CGLib'
      ],
      zip_safe=False)