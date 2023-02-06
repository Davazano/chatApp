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

while True:
    # Get input from user
    message = input(f'{my_username} :')

    if message:

        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        message = message.encode("utf-8")
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message)
    
    # Receive messages
    while True:

        username_header = client_socket.recv(HEADER_LENGTH)

        # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
        if not len(username_header):
            print('Connection closed by the server')
            sus.exit()

        # get username
        username_length = int(username_header.decode("utf-8").strip())
        username = client_socket.recv(username_length).decode("utf-8")

        # get message
        message_header = client_socket.recv(HEADER_LENGTH)
        message_length = int(message_header.decode('utf-8').strip())
        message = client_socket.recv(message_length).decode('utf-8')

        print(f"{username} :{message}")