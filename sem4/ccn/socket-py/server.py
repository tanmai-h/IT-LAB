import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as e:
    print(e)

try:
    s.bind(('', 1232))
    s.listen(4)    
except Exception as e:
    print(e)

def getter(file):
    try:
        s = ''
        with open(file, 'r') as f:
            s = f.readlines()
        f.close()
        s = ''.join(s)
        return s
    except Exception as e:
        return str(e)

while True:
    client, addr = s.accept()
    print('From ', addr)
    client.send('Connected'.encode())
    f = client.recv(1024).decode()
    client.send(getter(f).encode())
    client.close()
s.close()