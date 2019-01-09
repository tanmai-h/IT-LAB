import math
def strobo(n):
    f = 1
    a = int(math.pow(10,n))
    b = a*10 - 1
    
    g = str(n)
    for i in range(a, b+1):
        x = str(i)
        m = 0
        n = len(x)-1
        while m <= n/2:
            if (x[m] == '9' and x[n] == '6') or (x[m] == '6' and x[n] == '9') or (x[m] == '8' and x[n] == '8') or (x[m] == '0' and x[n] == '0') or (x[m] == '1' and x[n] == '1'):
                pass
            else:
                f = 0
                break
            m += 1
            n += -1
        if f is 1:
            print(i)
        f = 1           

n = int(input("Enter n: "))
strobo(n)