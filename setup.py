from setuptools import setup, find_packages

setup(
    name='example_submodule',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'redis~=2.10.6',
    ]

)
