import socket
import keyboard

# instantiate socket, socket.AF_INET for ipV4, SOCK_STREAM for TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket. Note you can use any free port. Sockets are endpoints that sends and receives data. Sockets are created using Ip address and port number
sock.bind((socket.gethostname(), 1233))
# listen (for incomming connections) using the socket. Queue of 5
sock.listen(5)

run_program = True
# continue to run until condition changes
while run_program:
    print(keyboard.read_key())
    if keyboard.read_key() == "Q":
        run_program = False
        print("Exiting Chat App")
        break