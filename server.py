import socket
import time
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1224))
s.listen(15)

HEADERSIZE = 10
while True:
    clientsocket, add = s.accept()
    print(f"connection from {add} has being established")

    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d)

    msg = bytes(f'{len(msg) :< {HEADERSIZE}}', "utf-8") + msg

    clientsocket.send(msg)
