"""
This script is used to install tweetlimiter and all its dependencies. Run

    python setup.py install
or
    python3 setup.py install

to install the package.
"""

# Copyright (C) 2022 Frank Sauerburger

from setuptools import setup

def load_long_description(filename):
    """
    Loads the given file and returns its content.
    """
    with open(filename, encoding="utf-8") as readme_file:
        content = readme_file.read()
        return content

setup(name='tweetlimiter',
      version='0.1.0',  # Also change in module
      packages=["tweetlimiter", "tweetlimiter.tests"],
      install_requires=["simple_pid"],
      test_suite='tweetlimiter.tests',
      description='Rate limit messages ',  # Short description
      long_description=load_long_description("README.rst"),
      url="https://gitlab.sauerburger.com/frank/tweetlimiter",
      author="Frank Sauerburger",
      author_email="frank@sauerburger.com",
      classifiers=[
          "Topic :: Communications",
          "Topic :: Scientific/Engineering :: Artificial Intelligence"
      ],
      license="MIT")
