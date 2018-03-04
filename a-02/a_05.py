#!/usr/bin/python

# Write a new script that takes three arguments as input. 
# The program should execute sequences of LED pulses using the previous given configuration:
# the first argument is the number of pulses contained by one sequence,
# the second argument is the interval (in seconds) between two pulses in a sequence 
# and the third argument is the pause period (in seconds) between two consecutive sequences.

import sys
import RPi.GPIO as GPIO