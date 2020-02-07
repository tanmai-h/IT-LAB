import random
import socket

def FiatShamirServer(AuthRound: tuple):
    N, v, y, x, c = AuthRound

    y_sqr_mod = pow(y, 2, N)

    test = (x * pow(v, c, N))%N

    print("c = ", c)
    print("y = ", y)
    print("y_sqr_mod = ", y_sqr_mod)
    print("test = ", test)

    assert y_sqr_mod == test, "y_sqr_mod != test"

def listen(port=1234):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print(e)    

    try:
        s.bind(('', port))
        s.listen(4)
    except Exception as e:
        print(e)

    return s

def main():
    sock = listen()
    client, addr = sock.accept()
    print("From: ", addr)
    
    N, v, c = -1, -1, 1

    print("recv N")
    N = client.recv(128).decode()

    print("recv v")
    v = client.recv(128).decode()

    print("recv x")
    x = client.recv(128).decode()

    # assert N != -1, "didnt get N"
    # assert v != -1, "didnt get v"

    print("Sending c")
    client.send(str(c).encode())
    y = client.recv(30).decode()

    client.close()
    sock.close()

    AuthRound = (int(N), int(v), int(y), int(x), c)

    FiatShamirServer(AuthRound)

if __name__ == '__main__':
    main()