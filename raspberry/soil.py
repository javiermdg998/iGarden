import RPi.GPIO as GPIO
import time
from datetime import datetime
import paho.mqtt.publish as publish
import json


channel=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
regado=False
def callback(channel):
    if GPIO.input(channel):
       regado=False
    else:
        regado=True
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel,callback)
while True:
    dateTimeObj = datetime.now()
    topic = "iGarden/values" 
    hostname = "test.mosquitto.org"
    mensaje ={"Humedadtierra":{"value":regado,
                     "TimeStamp":dateTimeObj}          
              }
    mensaje_json= json.dumps(mensaje)
    publish.single(topic, mensaje_json, hostname=hostname)
    time.sleep(1)
