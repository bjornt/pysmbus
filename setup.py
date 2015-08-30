from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name="pysmbus",
    version="0.1",
    description="Pure Python implementation of the I2C SMBus protocol.",
    long_description=readme,
    py_modules=["smbus"],
    include_package_data=True,
    zip_safe=True,
    url="https://github.com/bjornt/pysmbus",
    license="LGPL v2",
    author="Bjorn Tillenius",
    author_email="bjorn@tillenius.me",
    )
