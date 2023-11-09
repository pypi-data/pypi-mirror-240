# coding: utf-8

from setuptools import find_packages, setup

setup(
    name='evydcloud',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=["pandas", "pyhive", "pyjwt==1.6.4"],
    author='Yingjie Wang',
    author_email='yingjie.wang@evydtech.com',
    description='''DB Connector for Jupyter Notebook''',
    keywords='',
)
