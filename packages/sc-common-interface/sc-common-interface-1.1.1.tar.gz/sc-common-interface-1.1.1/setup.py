from setuptools import setup, find_packages

setup(
    name='sc-common-interface',
    version='1.1.1',
    description='SC公用的接口',
    author='river',
    packages=find_packages(),
    install_requires=[
    "requests>=2.0.0",
    "jsonpath>=0.82",


             ],
)
