from setuptools import setup

setup(
    name='menli',
    version='1.0.1',
    author='cyr',
    url='https://github.com/cyr19/MENLI',
    description='MENLI metrics v1',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=['menli'],
    install_requires=[
        'pandas',
        'scipy',
        'torch == 1.12.0',
        'transformers == 4.17.0',
        'bert_score == 0.3.11',
        'pyemd',
        'pytorch_pretrained_bert',
        'mosestokenizer'
    ]
)