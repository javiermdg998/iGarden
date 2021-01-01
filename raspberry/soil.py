import RPi.GPIO as GPIO
import time
from datetime import datetime
import paho.mqtt.publish as publish
import json
class Sensor_moisture():
    def callback(channel):
        if GPIO.input(channel):
            self.regado=False
        else:
            self.regado=True
    def read(self):
        return self.regado
    def __init__(self):
        channel=21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.IN)
        self.regado=False
        GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
        GPIO.add_event_callback(channel,self.callback)
    
