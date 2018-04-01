from firebase import firebase
import time


# the generated root for your project
FIREBASE_ROOT = 'https://ms-iot.firebaseio.com'
# init Firebase Database instance
firebase = firebase.FirebaseApplication(FIREBASE_ROOT, None)


while True:
    # execute a GET request on the node
    result = firebase.get('/sensor', None)
    # log the result
    print result
    # wait 1 second between two consecutive requests
    time.sleep(1)
