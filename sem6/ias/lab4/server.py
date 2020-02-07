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

    if y_sqr_mod != test:
        print("Invalid AUth")

        return False
    
    print("VAlid Auth")

    return True

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

    print("recv_Str")
    recv_str = client.recv(1024).decode()
    
    N, v, x = recv_str.split(':')

    print("Sending c")
    client.send(str(c).encode())
    y = client.recv(28).decode()

    AuthRound = (int(N), int(v), int(y), int(x), c)

    if FiatShamirServer(AuthRound):
        client.send("Valid auth!".encode())
    else:
        client.send("Invalid auth!".encode())

if __name__ == '__main__':
    main()