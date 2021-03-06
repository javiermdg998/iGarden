import RPi.GPIO as GPIO
class Led():
    def __init__(self, p):
        self.pin = p
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
    def encender_led(self):
        GPIO.output(self.pin, True)
    def apagar_led(self):
        GPIO.output(self.pin, False)