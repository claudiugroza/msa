#!/usr/bin/python

import RPi.GPIO as GPIO
import time

gpio_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_callback(pin):
	print 'Event occurred on pin ' + str(pin)

try:
	# apply 100ms debounce
	GPIO.add_event_detect(gpio_pin, GPIO.BOTH, callback=button_callback, bouncetime=100)

	print 'Start listening'
	
	# listen 20 seconds for events to be fired
	time.sleep(20)

finally:
	GPIO.remove_event_detect(gpio_pin)

	print 'Stop listening'
	GPIO.cleanup()