from setuptools import setup

setup(
    name='menli',
    version='1.0.0',
    author='cyr',
    url='https://github.com/cyr19/MENLI',
    description='MENLI metric v1',
    long_description='MENLI metrics',
    packages=['menli'],
    install_requires=[
        'pandas',
        'scipy',
        'torch == 1.12.0',
        'transformers == 4.17.0',
        'bert_score'
    ]
)