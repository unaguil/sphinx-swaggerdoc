import sys
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='sphinxcontrib-swaggerdoc',
    version='0.1.1',
    author='Unai Aguilera',
    author_email='unai.aguilera@deusto.es',
    description='Sphinx extension for documenting Swagger 2.0 APIs',
    long_description=read('README.rst'),
    license='MIT',
    keywords='',
    url='https://github.com/unaguil/sphinx-swaggerdoc',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities'
    ],
    packages=[
        'sphinxcontrib.swaggerdoc',
    ],
    install_requires=['sphinx', 'requests', 'requests-file', 'future']
)
