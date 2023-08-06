from setuptools import setup, find_packages

setup(name='MarkLib',
      version='1.1.3',
      description='',
      url='https://github.com/OGKG/PyMarkLib',
      author='Vsevolod Hermaniuk',
      author_email='shermanyuk@knu.ua',
      license='MIT',
    #   packages=['MarkLib'],
      install_requires=[
          'pydantic',
      ],
      packages=find_packages(),
      zip_safe=False)