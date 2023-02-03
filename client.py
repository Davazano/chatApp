import socket

# Constants
HEADER_SIZE = 20

# instantiate socket, socket.AF_INET for ipV4, SOCK_STREAM for TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server's socket (using Ip address and port number)
sock.connect((socket.gethostname(), 1233))

while True:

    full_msg = ''
    new_msg = True
    while True:
        # store buffered message
        msg = sock.recv(24)
        if new_msg:
            print(f"new message length: {msg[:HEADER_SIZE]}")
            msglen = int(msg[:HEADER_SIZE])
            new_msg = False
        
        full_msg += msg.decode("utf-8")

        # Check length of message
        if len(full_msg)-HEADER_SIZE == msglen:
            print("full msg recvd")
            # print message without header
            print(full_msg[HEADER_SIZE:])
            new_msg = True
            full_msg = ''

    print(full_msg)