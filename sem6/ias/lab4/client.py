import random
import socket
import math

def FiatShamir(AuthRound: tuple):
    N, r, s, c, sock = AuthRound

    y = (r * pow(s, c, N))%N
    
    sock.send(str(y).encode())
    
    return sock.recv(1024).decode()
    
def connect(host='127.0.0.1', port=1234):
    try: 
        s = socket.socket()
    except Exception as e:
        print(e)    

    s.connect((host, port))

    return s

def gcd(a, b): 
    if b == 0:
        return a
    else: return gcd(b, a%b)
    
def coprime(a, b):
    return gcd(a, b) == 1

def isPrime(num: int):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
            
    return True	

def main():
    sock = connect('192.168.177.128')

    print("---------------------------CLIENT-------------------------------\n")
    for i in range(1, 3+1):
        print("================Round:", i," ================")
        print("Enter P,Q, r, s: ")

        P, Q, r, s = map(int, list(input().split(' ')))
        
        N = P*Q
        print("\tN: ", N)
        if (not isPrime(P)) or (not isPrime(Q)):
            print("\tInvalid inpu: P, Q must be primes!")
            exit()
        if (r >= N):
            print("Invalid r input!. r must be 1 < r < N")
            exit()
        if (s >= N):
            print("Invalid s input!. s must be 1 < s < N")
            exit()            
        if (not coprime(N, r)) or (not coprime(N, s)):
            print("Invalid input!. s and r must be coprime to N")
            exit()
        
        v = pow(s, 2) % N
        x = pow(r, 2, N) % N    

        print("\tWitness: ", x)
        print("\tPublic Key: ", v)

        send_str = ':'.join([str(N), str(v), str(x)])

        # print("send_Str")
        sock.send(send_str.encode())    
    
        # print("recv c")
        c = int(sock.recv(28).decode()) 

        assert c != -1, "\tDidn't Receive Challenge"

        AuthRound = (N, r, s, c, sock)

        if not FiatShamir(AuthRound):
            print("\tStopping...")
            exit()
        
    sock.close()
    print("\n========================== Auth Succesful ======================")    

if __name__ == '__main__':
    main()