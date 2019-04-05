import socket
import _thread, threading

lock = threading.Lock()

def threaded(c):
    c.send('Connected'.encode())
    ch = c.recv(1024).decode()
    while True:
        if ch != 'exit':
            print(ch)
            c.send(ch[::-1].encode())
        else:
            lock.release()
            break
        ch = c.recv(1024).decode()
    c.close()

def main():    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print(e)
    try:
        s.bind(('', 1232))
        s.listen(4)    
    except Exception as e:
        print(e)

    while True:
        c,addr = s.accept()
        
        lock.acquire()
        print('from: ', addr)
        _thread.start_new_thread(threaded, (c,))
    
    s.close()

if __name__ == '__main__':
    main()