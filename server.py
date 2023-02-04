import socket
import select

# Constants
HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

# instantiate socket, socket.AF_INET for ipV4, SOCK_STREAM for TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SET SOCKET OPTION LEVEL's SOCKET OPTION REUSE ADDRESS TO TRUE. This allows reconnection
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind socket. Note you can use any free port. Sockets are endpoints that sends and receives data. Sockets are created using Ip address and port number
server_socket.bind((IP, PORT))
# listen (for incomming connections) using the socket. Queue of 5
server_socket.listen()

# list of clients
sockets_list = [server_socket]
# clients dictionary, key => client's socket, value => data from user

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        # if we didn't get any data. Probably due to client closing connection
        if not len(message_header):
            return False
        
        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:
        return False

