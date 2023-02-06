import socket
import select
import errno

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, PORT))

# set recv method to not blocking
client_socket.setblocking(False)

# set username
username = my_username.encode("utf-8")
# set username header
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
# send username
client_socket.send(username_header + username)

