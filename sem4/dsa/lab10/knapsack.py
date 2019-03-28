#knapsack
# val,weight = [],[]

def knapsack(i,w,dp):
    if i == -1 or w == 0:
        return 0
    if dp[i][weight[i]] != None:
        return dp[i][weight]
    if w-weight[i] > 0:
        dp[i][weight] = max(knapsack(i-1,w-weight[i],dp), knapsack(i-1,w,dp))
    else:
        dp[i][weight] = knapsack(i-1,w,dp)
        return dp[i][weight]
print('Enter values:')
val = [int(x) for x in input().split()]
print('Weights:')
weight = [int(x) for x in input().split()]

dp = [[None] for _ in range(len(val)) for _ in range(len(val))]
knapsack(len(val)-1,4,dp)
print(dp[-1][-1])
