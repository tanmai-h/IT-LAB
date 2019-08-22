import random
def lps(x):
    n = len(x)
    dp = [[0 for _ in range(len(x))] for _ in range(len(x))]    
    for i in range(n):
        dp[i][i] = 1
    for k in range(2,n+1):
        for i in range(n-k+1):
            j = i+k-1
            if x[i] == x[j] and k == 2:
                dp[i][j] = 2
            elif x[i] == x[j]:
                dp[i][j] = 2+dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
def lcs(x,y):
    dp = [[0 for _ in range(len(y)+1)] for _ in range(len(x)+1)]    
    c = 0
    a,b = 0,0
    for i in range(len(x)+1):
        for j in range(len(y)+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if c < dp[i][j]:
                    c = dp[i][j]
                    a,b = i,j
            else:
                dp[i][j] = 0
    s = []
    for i in dp:
        print(i)
    while dp[a][b] != 0:
        s.append(x[a-1])
        a -= 1
        b -= 1
    s.reverse()
    print(s)

def part(l,i,j):
    p = l[-1]
    s = i-1
    for e in range(i,j):
        print(i,j)
        if l[e] < p:
            i += 1
            l[i],l[e] = l[e],l[i]
    l[i+1],l[j], = l[j],l[i+1]
    return i+1

def kth(l,i,j,k):
    p = random.randint(i,j)
    l[p],l[-1] = l[-1],l[p]
    q = part(l,i,j)

    if k-1 < q-i:
        kth(l,i,q-1,k)
    elif k-1 == q-i:
        return q
    else:
        kth(l,q+1,j,k-q+i-1)

l = [12, 3, 5, 7, 4, 19, 26]
print(l[kth(l,0,len(l)-1,3)])