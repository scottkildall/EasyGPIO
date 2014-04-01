# gpio_blink.py
# by Scott Kildall (www.kildall.com)
# LED is on pin 4, use a 270 Ohm reistor to ground

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

state = True

# endless loop, on/off for 1 second
while True:
	GPIO.output(4,True)
	time.sleep(1)	
	GPIO.output(4,False)
	time.sleep(1)
