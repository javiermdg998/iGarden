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
import soil
s_humi_temp = get_humi_temp.Sensor_temp_hum()
s_lum = get_lumi.Sensor_lum()
s_mois=soil.Sensor_moisture()
while True:
    humi, temp = s_humi_temp.read()
    #Las variables humi y temp tienen los datos de humedad y temperatura respectivamente.
    
    EV = s_lum.read()
    #EV tiene los luxes del espectro visible
    mois=s_mois.read()

    dateTimeObj = datetime.now()
    dateTimeObj=str(dateTimeObj)
    topic = "iGarden/values" 
    hostname = "test.mosquitto.org"

    mensaje ={
     "humedad":humi,
     "temperatura":temp,
     "luminosidad":EV,
     "fecha":dateTimeObj,
     "humid":mois
    }
    mensaje_json= json.dumps(mensaje)
    publish.single(topic, mensaje_json, hostname=hostname)
    print(mensaje)
    time.sleep(3)