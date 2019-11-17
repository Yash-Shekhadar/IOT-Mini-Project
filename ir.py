import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

def irsensor():
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(2,GPIO.OUT) #GPIO 2 -> buzzer as output
	GPIO.setup(14,GPIO.IN) #GPIO 14 -> IR sensor1 as input
	GPIO.setup(15,GPIO.IN) #GPIO 15 -> IR sensor2 as input
	GPIO.setup(18,GPIO.IN) #GPIO 18 -> IR sensor3 as input

	while 1:
		if(GPIO.input(14)==True or GPIO.input(15)==True or GPIO.input(18)==True): #object is far away
			#print("object is far away")
			GPIO.output(2,GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(2,GPIO.LOW)
			time.sleep(0.1)
		
		if(GPIO.input(14)==False and GPIO.input(15)==False and GPIO.input(18)==False): #object is near 
			#print("object is near")
			GPIO.output(2,GPIO.LOW)
			#return
			#time.sleep(5)
	GPIO.cleanup()
irsensor()	
