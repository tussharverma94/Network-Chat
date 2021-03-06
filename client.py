import socket
import pickle
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1224))

HEADERSIZE = 10

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"New message length: {msg[:HEADERSIZE]}")
            msg_len = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADERSIZE == msg_len:
            print("Full message recived")
            print(full_msg[HEADERSIZE:])

            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b''

    print(full_msg)
