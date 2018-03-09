import zmq
import sys
from threading import Thread

# ZeroMQ Context
context = zmq.Context()

# TODO: change this to PUB pattern.
# Define the socket using the "Context"
sub_sock = context.socket(zmq.SUB)
sub_sock.setsockopt_string(zmq.SUBSCRIBE, "")
sub_sock.connect("tcp://127.0.0.1:5678")

req_sock = context.socket(zmq.REQ)
req_sock.connect("tcp://127.0.0.1:5680")
# Send a "message" using the socket

def subscribe():
    while True:
        sub_msg = sub_sock.recv()
        print(sub_msg.decode())


req_msg = " ".join(sys.argv[1:])

t = Thread(target=subscribe)
t.start()
print("User [" + req_msg + "] connected to the chat server.")

try:
    while True:
        content = input(">" )
        req_sock.send_string("[" + req_msg + "]: " + content)
        message = req_sock.recv()
except KeyboardInterrupt:
        print("quit")
        exit(0)
