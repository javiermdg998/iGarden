import RPi.GPIO as GPIO 
import dht_config
class Sensor_temp_hum():
    def init(self):
        GPIO.setmode(GPIO.BCM)
        gpio_pin_sensor = 18
        self.sensor = dht_config.DHT(gpio_pin_sensor)

    def leer(self):
        humi, temp = self.sensor.read()
        return humi, temp

sensor = Sensor_temp_hum() 
h,t=sensor.leer()
print("humi : " + h+ ".  Temp : " + t)