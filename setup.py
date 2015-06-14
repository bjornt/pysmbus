from setuptools import setup

setup(
    name="pysmbus",
    version="0.1",
    description="Pure Python implemetation of the I2C SMBus protocol.",
    py_modules=["smbus"],
    include_package_data=True,
    zip_safe=True,
    )
