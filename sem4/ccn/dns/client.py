import socket

buffer_length = 1024
port = 8080

try:
    s = socket.socket()
except Exception as e:
    print(e)

try:
    s.connect(('127.0.0.1', port))
except Exception as e:
    print(e)

print(s.recv(buffer_length).decode())
s.send(input().encode())
print(s.recv(buffer_length).decode())