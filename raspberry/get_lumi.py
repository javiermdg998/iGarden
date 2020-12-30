import RPi.GPIO as GPIO
import smbus
import dht_config

class Sensor_lum():
    def init(self):
        bus = smbus.SMBus(1)
        TSL2561_DEFAULT_ADDRESS = 0x29
        bus.write_byte_data(TSL2561_DEFAULT_ADDRESS, 0x00 | 0x80, 0x03)
        bus.write_byte_data(TSL2561_DEFAULT_ADDRESS, 0x01 | 0x80, 0x01)
        self.data = bus.read_i2c_block_data(TSL2561_DEFAULT_ADDRESS, 0x0C | 0x80, 2)
        self.data1 = bus.read_i2c_block_data(TSL2561_DEFAULT_ADDRESS, 0x0E | 0x80, 2)

    def read(self):
        ch0 = self.data[1] * 256 + self.data[0] 
        ch1 = self.data1[1] * 256 + self.data1[0] 
        ev = ch0-ch1
        return ev
        
sensor = Sensor_lum() 
ev = sensor.read()
print("luz = " + ev)

