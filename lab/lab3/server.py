
import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
pub_sock = context.socket(zmq.PUB)
pub_sock.bind("tcp://127.0.0.1:5678")

rep_sock = context.socket(zmq.REP)
rep_sock.bind("tcp://127.0.0.1:5680")

# Run a simple "Echo" server
try:
    while True:
        rep_msg = rep_sock.recv()
        rep_msg = rep_msg.decode()
        rep_sock.send_string(rep_msg)

        pub_sock.send_string(rep_msg)
except KeyboardInterrupt:
        print("quit")
        exit(0)