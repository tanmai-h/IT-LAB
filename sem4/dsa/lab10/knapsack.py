#knapsack
val,weight = [],[]

def knapsack(i,w,dp): 
    if i == -1 or w == 0:
        return 0
    if dp[i][w] != None:
        return dp[i][w]
    
    elif weight[i] > w:
        dp[i][w] = knapsack(i-1,w,dp)
    else:
        dp[i][w] = max(val[i]+knapsack(i-1,w-weight[i],dp), knapsack(i-1,w,dp))

    return dp[i][w]

print('Enter values:')
val = [int(x) for x in input().split()]
print('Weights:')
weight = [int(x) for x in input().split()]
maxwt = int(input('Max weight of bag\n'))

dp = [[None for _ in range(maxwt+1)] for _ in range(len(val))]
knapsack(len(val)-1, maxwt, dp)
print(dp[-1][-1])