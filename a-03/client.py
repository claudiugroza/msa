import socket
import sys
import json
import time


def send(server_address, state):
    #  create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # start a connection
    sock.connect(server_address)
    try:
        # prepare a dictionary
        value = {'state' : state}
        # encode object
        encoded_object = json.dumps(value)
        # send data
        sock.sendall(encoded_object)
        print '{} sent {}'.format(time.strftime("%H:%M:%S"), encoded_object)
    finally:
        print 'closing socket'
        sock.close()


# connection tuple
server_address = ('localhost', 1221)
# send a '1' command
send(server_address, 1)
