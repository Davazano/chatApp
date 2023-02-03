import socket

# instantiate socket, socket.AF_INET for ipV4, SOCK_STREAM for TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server's socket (using Ip address and port number)
sock.connect((socket.gethostname(), 1233))

full_msg = ''
while True:
    # store buffered message
    msg = sock.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)