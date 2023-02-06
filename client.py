import socket
import select
import errno

HEADER_LENGTH = 10