from setuptools import setup, find_packages

setup(
    name='vectoriadb-protocol-wrapper',
    version='0.1.0.dev1',
    packages=find_packages(),
    install_requires=[
        'protobuf>=4.25.0',
        'grpcio>=1.59.2',
    ],
    include_package_data=True,
    url='https://github.com/JetBrains/xodus',
    license='Apache License 2.0',
    zip_safe=False
)
