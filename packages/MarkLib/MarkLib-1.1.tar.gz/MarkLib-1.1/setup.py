from setuptools import setup

setup(name='MarkLib',
      version='1.1',
      description='',
      url='https://github.com/OGKG/PyMarkLib',
      author='Vsevolod Hermaniuk',
      author_email='shermanyuk@knu.ua',
      license='MIT',
      packages=['MarkLib'],
      install_requires=[
          'pydantic',
      ],
      zip_safe=False)