import RPi.GPIO as GPIO
class led():
    def __init__(self, p):
        self.pin = p
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
    def encender_led(self):
        GPIO.output(self.pin, True)
    def apagar_led(self):
        GPIO.output(self.pin, False)