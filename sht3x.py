# MIT License
#
# Copyright (c) for portions of this library are held by HAIZAKURA, 2020, who is
# the original author of the esp-sht3x-micropython library.
#
# All other copyright (c) for this library are by Florian Volk, 2021.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# adapted from HAIZAKURA's library found at https://github.com/HAIZAKURA/esp-sht3x-micropython
# adapted by Florian Volk @digitalvolk (digitalvolk.de)
# changes:
# - __init__ adapted for supplying already existing i2c object (useful when there are multiple devices on the bus)
# - read_temp_humd adapted to select Celsius or Farenheit scale


import utime


class SHT3x_Sensor:

    def __init__(self, i2c, addr=0x44):
        self.i2c = i2c
        self.addr = addr

    def read_temp_humd(self, celsius=True):
        status = self.i2c.writeto(self.addr, b'\x24\x00')
        # delay (20 slow)
        utime.sleep(1)
        # read 6 bytes
        databytes = self.i2c.readfrom(self.addr, 6)
        dataset = [databytes[0], databytes[1]]
        dataset = [databytes[3], databytes[4]]
        temperature_raw = databytes[0] << 8 | databytes[1]
        temperature = (175.0 * float(temperature_raw) / 65535.0) - 45 if celsius else (315.0 * float(temperature_raw) / 65535.0) - 49
        humidity_raw = databytes[3] << 8 | databytes[4]
        humidity = (100.0 * float(humidity_raw) / 65535.0)
        sensor_data = [temperature, humidity]
        return sensor_data
