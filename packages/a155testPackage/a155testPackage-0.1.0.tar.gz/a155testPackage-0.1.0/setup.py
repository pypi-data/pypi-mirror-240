from setuptools import setup, find_packages

setup(
    name='a155testPackage',
    version='0.1.0',
    description='A short description of your package',
    packages=find_packages(),
    install_requires=['ipfshttpclient==0.8.0a2','web3', 'requests'],
    classifiers=[
        'Programming Language :: Python :: 3.12'
    ]
)