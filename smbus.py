import posix
from fcntl import ioctl
from ctypes import c_char, c_int, c_uint8, POINTER, Structure, byref

I2C_SLAVE = 0x0703
I2C_SMBUS = 0x0720
I2C_SMBUS_WRITE = 0
I2C_SMBUS_BYTE_DATA = 2

LP_c_uint8 = POINTER(c_uint8)

class i2c_smbus_msg(Structure):

    _fields_ = [
        ('read_write', c_char),
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

    def write_byte_data(self, i2c_addr, cmd, value):
        self._set_addr(i2c_addr)
        msg = i2c_smbus_msg(
            read_write=I2C_SMBUS_WRITE, command=cmd, size=I2C_SMBUS_BYTE_DATA,
            data=LP_c_uint8(c_uint8(value)))
        ioctl(self.fd, I2C_SMBUS, msg)
