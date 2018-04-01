from firebase import firebase
import time
import socket


# generated root for your project
FIREBASE_ROOT = 'https://ms-iot.firebaseio.com'
# init Firebase Database instance
firebase = firebase.FirebaseApplication(FIREBASE_ROOT, None)
# find a local 'unique' name
BOARD_NAME = socket.gethostname()


def write_button_state(state):
    # build the node to be pushed
    value = {BOARD_NAME : state}
    # prefer update of the node
    result = firebase.patch('/boards', value)
    print result


# mock a value and then push 
write_button_state('UNKNOWN')
