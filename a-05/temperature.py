import random

START   = -5;
STOP    = 30;

# stub for temperature sensor
def read_temp():
    temp = random.randrange(START, STOP)
    return temp