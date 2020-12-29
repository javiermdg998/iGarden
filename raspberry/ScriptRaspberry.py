import RPi.GPIO as GPIO
import time
import smbus
import dht_config
import paho.mqtt.publish as publish
import json
import sys
from datetime import datetime
import get_humi_temp
import get_lumi

s_humi_temp = get_humi_temp.Sensor_temp_hum()
humi, temp = s_humi_temp.leer()
#Las variables humi y temp tienen los datos de humedad y temperatura respectivamente.
s_lum = get_lumi.Sensor_lum()
EV = s_lum.read()
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
