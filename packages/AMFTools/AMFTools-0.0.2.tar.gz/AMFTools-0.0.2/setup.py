from setuptools import setup, find_packages

setup(
  name = "AMFTools",
  version = "0.0.2",
  author="PaulGrx_AMF",
  license='proprietary license (Advanced Microfluidics SA)',
  description='AMF Tools is a python package that will made you able to controle all Advanced Microfluics SA. devices',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='https://amf.ch',
  packages=find_packages(exclude=["testing"]),
  install_requires=[
    'pyserial',
    'ftd2xx',
  ],
  python_requires='>=3.8',
  classifiers=[
    "Programming Language :: Python :: 3",
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3.11",
    "Topic :: Security"
  ],
)