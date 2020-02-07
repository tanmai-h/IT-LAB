import random
import socket

def FiatShamir(AuthRound: tuple):
    N, r, s, c, sock = AuthRound
    
    x = pow(r, 2, N) % N
    v = pow(s, 2, N) % N

    print("N = ", N)
    print("s = ", s)
    print("v = ", v)
    print("r = ", r)
    print("x = ", x)

    y = (r * pow(s, c, N))%N
    
    sock.send(str(y).encode())
    
    print(sock.recv(1024).decode())
    
def connect(host='127.0.0.1', port=1234):
    try: 
        s = socket.socket()
    except Exception as e:
        print(e)    

    s.connect((host, port))

    return s

def main():
    sock = connect()

    P, Q = 467, 479
    N = P*Q
    r, s, c = 1111, 111, -1
    v = pow(s, 2) % N
    x = pow(r, 2, N) % N

    send_str = ':'.join([str(N), str(v), str(x)])

    print("send_Str")
    sock.send(send_str.encode())    
    
    print("recv c")
    c = int(sock.recv(28).decode()) 

    assert c != -1, "Didn't Receive Challenge"

    AuthRound = (N, r, s, c, sock)

    FiatShamir(AuthRound)

if __name__ == '__main__':
    main()