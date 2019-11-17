
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)

def buzz():
	gpio.setmode(gpio.BCM)
	gpio.setup(2,gpio.OUT) #GPIO 2 -> buzzer as output
	gpio.output(2,False)
	gpio.output(2,True)
	time.sleep(0.2)
	gpio.output(2,False)
	gpio.cleanup()
	#return
buzz()
