"""pysmbus - A ure Python implementation of the I2C SMBus protocol."""
# Copyright (C) 2015  Bjorn Tillenius <bjorn@tilenius.me>
#
# This library is free software; you can redistribute it and/or
# # modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation;
# version 2 of the License.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.

# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301  USA


import posix
import struct
from fcntl import ioctl
from ctypes import c_int, c_uint8, POINTER, Structure


I2C_SLAVE = 0x0703
I2C_SMBUS = 0x0720
I2C_SMBUS_WRITE = 0
I2C_SMBUS_READ = 1
I2C_SMBUS_BYTE_DATA = 2

LP_c_uint8 = POINTER(c_uint8)


class i2c_smbus_msg(Structure):

    _fields_ = [
        ('read_write', c_uint8),  # Should be c_char, but c_uint8 is the
                                  # same size is makes it easier to
                                  # support both Python 2.7 and 3.x.
        ('command', c_uint8),
        ('size', c_int),
        ('data', LP_c_uint8)]

    __slots__ = [name for name,type in _fields_]


class SMBus(object):

    def __init__(self, bus):
        self.fd = posix.open("/dev/i2c-{}".format(bus), posix.O_RDWR)
        self.addr = None

    def _set_addr(self, addr):
        if self.addr != addr:
            ioctl(self.fd, I2C_SLAVE, addr);

    def write_byte_data(self, i2c_addr, register, value):
        """Write a single byte to a designated register."""
        self._set_addr(i2c_addr)
        byte_value = c_uint8(value)
        data_pointer = LP_c_uint8(byte_value)
        msg = i2c_smbus_msg(
            read_write=I2C_SMBUS_WRITE, command=register,
            size=I2C_SMBUS_BYTE_DATA, data=data_pointer)
        ioctl(self.fd, I2C_SMBUS, msg)

    def read_byte_data(self, i2c_addr, register):
        """Read a single byte from a designated register."""
        self._set_addr(i2c_addr)
        data_pointer = LP_c_uint8(c_uint8())
        msg = i2c_smbus_msg(
            read_write=I2C_SMBUS_READ, command=register,
            size=I2C_SMBUS_BYTE_DATA, data=data_pointer)
        ioctl(self.fd, I2C_SMBUS, msg)
        [result] = struct.unpack("@b", data_pointer.contents)
        return result
