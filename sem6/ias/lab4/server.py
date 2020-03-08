import random
import socket

def FiatShamirServer(AuthRound: tuple):
    N, v, y, x, c = AuthRound

    y_sqr_mod = pow(y, 2, N)
    test = (x * pow(v, c, N))%N

    print("\tY^2 mod n = ", y_sqr_mod)
    print("\tXV^2 mod n = ", test)

    if y_sqr_mod != test:
        return False

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
    
    print("---------------------------SERVER-------------------------------")

    for i in range(1, 3+1):
        print("================Round:", i," ================")
        
        print("Enter challenge c: ")
        c = int(input())

        # print("\trecv_Str")
        recv_str = client.recv(1024).decode()
    
        try:
            N, v, x = recv_str.split(':')
        except Exception as e:
            print("--------------------- Aborting... ------------")
            sock.close()
            client.close()
            exit(-1)
        # print("\tSending c")
        client.send(str(c).encode())
        
        y = client.recv(28).decode()

        AuthRound = (int(N), int(v), int(y), int(x), c)

        if not FiatShamirServer(AuthRound):
            client.send(str(False).encode())
            client.close()
            print("\tWrong/Invalid Response from Client. Aborting...")
            exit()

        else:
            print("\tCorrect response for challenge in round ", i)
            client.send(str(True).encode())

    print("=======================Claiment Auth Succesful!=======================")

if __name__ == '__main__':
    main()