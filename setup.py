import sys
from setuptools import setup
# from tests import PyTest

setup(
    name='sphinx_swagger',
    version='0.1.0',
    packages=[
        'sphinx_swagger',
    ],

    url='',
    license='MIT',
    author='Unai Aguilera',
    author_email='unai.aguilera@deusto.es',
    description='Sphinx extension that automatically documents Swagger APIs',
    long_description='',
    install_requires=['sphinx', 'requests']
)
