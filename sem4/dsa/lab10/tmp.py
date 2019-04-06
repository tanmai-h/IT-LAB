def lcs(x:str,y:str, i, j, dp):
    if i == -1 or j == -1:
        return 0
    if dp[i][j] != None:
        return dp[i][j]
    else:
        if x[i] == y[j]:
            dp[i][j] = 1 + lcs(x,y,i-1,j-1,dp)
        else:
            dp[i][j] = max(lcs(x,y,i-1,j,dp), lcs(x,y,i,j-1,dp))
    return dp[i][j]

dp = [[0 for _ in range(7)] for _ in range(6)]
print(lcs('AGGTAB','GXTXAYB',5,6,dp))
for i in dp:
    print(i)
