import RPi.GPIO as GPIO
import time
import smbus
import dht_config
import paho.mqtt.publish as publish
import json
import sys
from datetime import datetime


GPIO.setmode(GPIO.BCM)
gpio_pin_sensor = 18   
sensor = dht_config.DHT(gpio_pin_sensor) 
humi, temp = sensor.read()
#Las variables humi y temp tienen los datos de humedad y temperatura respectivamente.

bus = smbus.SMBus(1)
TSL2561_DEFAULT_ADDRESS = 0x29
bus.write_byte_data(TSL2561_DEFAULT_ADDRESS, 0x00 | 0x80, 0x03)
bus.write_byte_data(TSL2561_DEFAULT_ADDRESS, 0x01 | 0x80, 0x01)
data = bus.read_i2c_block_data(TSL2561_DEFAULT_ADDRESS, 0x0C | 0x80, 2)
data1 = bus.read_i2c_block_data(TSL2561_DEFAULT_ADDRESS, 0x0E | 0x80, 2)
ch0 = data[1] * 256 + data[0] 
ch1 = data1[1] * 256 + data1[0] 
EV = ch0-ch1
#EV tiene los luxes del espectro visible 

dateTimeObj = datetime.now()
topic = "iGarden/values" 
hostname = "test.mosquitto.org"
mensaje ={"Humedad":{"value":humi,
                     "TimeStamp":dateTimeObj},
          "Temperatura":{"value":temp,
                     "TimeStamp":dateTimeObj},
          "Luz":{"value":EV,
                     "TimeStamp":dateTimeObj}
}

mensaje_json= json.dumps(mensaje)
publish.single(topic, mensaje_json, hostname=hostname)
