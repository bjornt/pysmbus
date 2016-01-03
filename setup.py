from setuptools import setup

readme = """

=======

The pysmbus package is a pure Python reimplentation of the
[python-smbus](http://www.lm-sensors.org/browser/i2c-tools/trunk/py-smbus/)
package. This allows using the I2C SMBus protocol without having to compile C.

It has the same module name, `smbus`, as `python-smbus`, so that it can
be used as a direct replacement in projects that normally depend on
`python-smbus`.

Currently it's incomplete. The following methods are implemented:

    * write_byte_data
    * read_byte_data

Other methods haven't been implemented yet, since I don't have any hardware
needing those methods. Patches or requests for other methods are welcome.

This package has been comfirmed working with Python 2.7 and 3.4.


Example
-------

    from smbus import SMBus

    bus = SMBus(1)  # Opens /dev/i2c-1
    bus.write_byte_data(0x54, 0x13, 0xff)

"""

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
