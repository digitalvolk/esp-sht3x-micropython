# esp-sht3x-micropython

An SHT3x (SHT30/31/35) lib for esp8266/esp32 with MicroPython.

Forked from [HAIZAKURA](https://nya.run) (https://github.com/HAIZAKURA/esp-sht3x-micropython), released under the [MIT](./LICENSE) License.

Adapted for easier and more flexible use. Can be used together with other i2c devices on the same bus.

## Usage

```python
from machine import Pin, SoftI2C
import sht3x

i2c = SoftI2C(scl=Pin(25), sda=Pin(26)) # change pins according to your board

sht3x = sht3x.SHT3x_Sensor(i2c)
temperature, humidity = sht3x.read_temp_humd()

print("Temperature: " + str(temperature) + " °C")
print("Humidity: " + str(humidity) + " %")

```

## Notice

Use `read_temp_humd(celsius=False)` to read the temperature in degrees Fahrenheit. 
