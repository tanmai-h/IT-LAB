#socket - client

import socket
import sys

try:
    s = socket.socket()
except Exception as e:
    print(e)

port = 1232

s.connect(('127.0.0.1', port))
print(s.recv(1024).decode())
ch = input()
while True:
    s.send(ch.encode())
    if ch == 'exit':
        break
    else:
        print(s.recv(1024).decode())
    ch = input()
# print(s.recv(10240).decode())
