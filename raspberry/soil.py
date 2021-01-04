import RPi.GPIO as GPIO
import time
from datetime import datetime
from datetime import timedelta
import paho.mqtt.publish as publish
import json
class Sensor_moisture():
    def callback(self,channel):
        self.regado=True
        self.ult_reg=datetime.now()
    def read(self):
        if datetime.now()-self.ult_reg>self.delta:
            self.regado=False
        return self.regado
    def __init__(self):
        self.ult_reg=datetime.now()
        self.delta=timedelta(seconds=3)
        channel=21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.IN)
        self.regado=False
        GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
        GPIO.add_event_callback(channel,self.callback)

