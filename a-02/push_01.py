#!/usr/bin/python

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		print GPIO.input(12)

finally:
	GPIO.cleanup()