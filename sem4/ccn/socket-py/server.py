#socket - server 

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as e:
    print("cant create socket", e)

port = 1230

try:
    s.bind(('', port))
except Exception as e:
    print(e)
s.listen(5)

#while True:
client, addr = s.accept()
print("connection from: ", addr)
client.send("u connected to the server".encode())

print(client.recv(1024).decode())

client.close()

s.close()
