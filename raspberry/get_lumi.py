import RPi.GPIO as GPIO
import smbus
import dht_config

class Sensor_lum():
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.TSL2561_DEFAULT_ADDRESS = 0x29
        self.bus.write_byte_data(self.TSL2561_DEFAULT_ADDRESS, 0x00 | 0x80, 0x03)
        self.bus.write_byte_data(self.TSL2561_DEFAULT_ADDRESS, 0x01 | 0x80, 0x01)
    

    def read(self):
        data = self.bus.read_i2c_block_data(self.TSL2561_DEFAULT_ADDRESS, 0x0C | 0x80, 2)
        data1 = self.bus.read_i2c_block_data(self.TSL2561_DEFAULT_ADDRESS, 0x0E | 0x80, 2)
        ch0 = data[1] * 256 + data[0] 
        ch1 = data1[1] * 256 + data1[0] 
        ev = ch0-ch1
        return ev
        
sensor = Sensor_lum() 
ev = sensor.read()
print("luz = " + str(ev))

