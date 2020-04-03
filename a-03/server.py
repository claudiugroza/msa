import RPi.GPIO as GPIO
import socket
import sys
import json
import time


def setup_gpio(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)


def set_output(pin, value):
    print('setting {} to pin {}'.format(value, pin))
    GPIO.output(pin, value)


def listen(server_address, pin):
    # create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # associate socket with server address
    sock.bind(server_address)
    # start listening for incoming connections
    sock.listen(5)

    while True:
        print('waiting connection')
        connection, client_address = sock.accept()

        buff = b''
        try:
            print('{} connected to {}'.format(time.strftime("%H:%M:%S"), client_address))
            while True:
                # receive data in chunks
                data = connection.recv(8)
                if data:
                    buff += data
                else:
                    break
            # parse received data
            json_recv = json.loads(buff.decode('utf-8'))
            # extract state value
            state = json_recv['state']
            # write LED state
            set_output(pin, state)
        finally:
            print('{} disconnected from {}'.format(time.strftime("%H:%M:%S"), client_address))
            connection.close()


try:
    # associated pin number for LED
    pin = 12
    # provide address as  a tuple
    server_address = ('localhost', 1221)
    # configure LED
    setup_gpio(pin)
    # listen and react on client requests
    listen(server_address, pin)
finally:
    GPIO.cleanup()
