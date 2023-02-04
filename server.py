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


while True:
    
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        # if someone just connected
        if notified_socket == server_socket:
            # accept connection
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            # someone probably disconected
            if user is False:
                continue
            
            sockets_list.append(client_socket)

            clients[client_socket] = user

            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")

        else:
            message = receive_message(notified_socket)

            if message is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            
            user = clients[notified_socket]
            print(f"Recieved message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

            for client_socket in clients:
                # send to other clients other than the client that sent the message
                if client_socket != notified_socket:
                    client_socket.send(user["header"] + user["data"] + message['header'] + message['data'])
    
    