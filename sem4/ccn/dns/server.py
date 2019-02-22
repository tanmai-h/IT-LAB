import socket
import sys

buffer_length = 1024
port = 8080

try:
    s = socket.socket()
except Exception as e:
    print(e)

try:
    s.bind(('', port))
    s.listen(3)
except Exception as e:
    print(e)

while True:
    client, addr = s.accept()
    print("received connection: ", addr)
    
    client.send("Provide url".encode())
    url = client.recv(buffer_length).decode()
    ip_addr = socket.gethostbyname(url)

    client.send(str(ip_addr).encode())

    client.close()