# get LIS = longest increasing sub sequence
def LIS(l,dp,next):
    n = len(l)
    for i in range(n-1,-1,-1):
        m = 1
        for j in range(i+1,n,1):
            if l[i] < l[j]:
                if (1+dp[j] > m):
                    m = 1 + dp[j]
                    next[i] = j
        dp[i] = m

    i = dp.index(max(dp))
    t = []
    while True:
        t.append(l[i])
        if next[i] == -1:
            break
        i = next[i]
    
    print('Length of LIS', max(dp))
    print(t)
    
def main():
    l = [10,22,9,33,21,50,41,60,80]#[5,2,8,6,3,6,9,7]#[int(x) for x in input().split()]
    dp = [0 for _ in range(len(l))]

    next = [-1 for _ in range(len(l))]
    LIS(l,dp,next)    
if __name__ == '__main__':
    main()