import random
import socket

def FiatShamir():
    P, Q = 467, 497
    r, s, c = 1111, 111, 1
    N = P * Q
    
    x = pow(r, 2, N)
    v = pow(s, 2, N)

    print("N = P*Q = ", N)
    print("s = ", s)
    print("v = ", v)
    print("r = ", r)
    print("x = ", x)

    e = random.randint(0, 1)
    y = (r * pow(s, e, N))%N

    y_sqr_mod = pow(y, 2, N)
    test = (x * pow(v, e, N))%N

    print("e = ", e)
    print("y = ", y)
    print("y_sqr_mod = ", y_sqr_mod)
    print("test = ", test)
    assert y_sqr_mod == test, "y_sqr_mod != test"

def main():
    FiatShamir()
    exit()
    try: 
        s = socket.socket()
    except Exception as e:
        print(e)    

    port = 1232

    s.connect(('127.0.0.1'), port)

if __name__ == '__main__':
    main()