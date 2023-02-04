import socket
import keyboard
import time
import pickle

# code for new branch

# Constants
HEADER_SIZE = 20

# instantiate socket, socket.AF_INET for ipV4, SOCK_STREAM for TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket. Note you can use any free port. Sockets are endpoints that sends and receives data. Sockets are created using Ip address and port number
sock.bind((socket.gethostname(), 1233))
# listen (for incomming connections) using the socket. Queue of 5
sock.listen(5)

run_program = True
# continue to run until condition changes
while run_program:
    print("waiting for client")
    # print key pressed
    print(keyboard.read_key())

    # check if keypressed is 'Q'
    if keyboard.read_key() == "Q":
        # change state run_program to False
        run_program = False
        # print message showing that chat app is closed
        print("Closed Chat App")
        break
    
    # accept connections, store clientsocket, and ip address
    clientsocket, address = sock.accept()

    print(f"Established connection with {address}!")

    # Form a message with the fixed length header
    d = {1: "Hey",  2: "There"}
    msg = pickle.dumps(d)

    msg = bytes(f'{len(msg):<{HEADER_SIZE}}', "utf-8") + msg

    # send information to the client socket
    clientsocket.send(msg)
