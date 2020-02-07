import random
import socket

def FiatShamir(AuthRound: tuple):
    N, r, s, c, sock = AuthRound

    # P, Q = 467, 497
    # r, s, c = 1111, 111, 1
    # N = P * Q
    
    x = pow(r, 2, N)
    v = pow(s, 2, N)

    print("N = ", N)
    print("s = ", s)
    print("v = ", v)
    print("r = ", r)
    print("x = ", x)

    y = (r * pow(s, c, N))%N
    
    sock.send(str(y).encode())
    
    # y_sqr_mod = pow(y, 2, N)

    # test = (x * pow(v, c, N))%N

    # print("c = ", c)
    # print("y = ", y)
    # print("y_sqr_mod = ", y_sqr_mod)
    # print("test = ", test)

    # assert y_sqr_mod == test, "y_sqr_mod != test"

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
    x = pow(r, 2, N)

    print("send N")
    sock.send(str(N).encode()) #Send N

    print("send v")
    sock.send(str(v).encode()) # Send v = s^2 % N

    print("send x")
    sock.send(str(x).encode()) 
    
    print("recv c")
    c = sock.recv(512).decode()    #Receive challenge c

    assert c != -1, "Didn't Receive Challenge"

    AuthRound = (N, r, s, c, sock)

    # print(AuthRound)
    FiatShamir(AuthRound)

if __name__ == '__main__':
    main()