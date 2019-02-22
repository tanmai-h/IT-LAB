#socket - client

import socket
import sys

try:
    s = socket.socket()
except Exception as e:
    print(e)

port = 1230

s.connect(('127.0.0.1', port))
print(s.recv(1024).decode())
s.send(input().encode())

