#!/usr/bin/python

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12, 50)

try:
	pwm.start(50)

	time.sleep(5)

finally:
	GPIO.cleanup()