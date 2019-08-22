# Edit_util distance of 2 strings

def diff(x:str,y:str,i,j):
    if x[i] == y[j]:
        return 0
    else:
        return 1

def Edit(x:str,y:str):
    ''' Top Down Approach, prev states stored in dp[n][m] '''
    dp = [[None for j in range(len(y)+1)] for i in range(len(x)+1)]

    return Edit_util(x,y,len(x),len(y),dp)
    
def Edit_util(x:str,y:str,i,j,dp): 
    if dp[i][j] != None:
        return dp[i][j]
    else:
        if i == 0:
            return j
        elif j == 0:
            return i

        e = min(diff(x,y,i-1,j-1) + Edit_util(x,y,i-1,j-1,dp), 
                1+Edit_util(x,y,i,j-1,dp),
                1+Edit_util(x,y,i-1,j,dp)
                )
        dp[i][j] = e

        return e

def EditBottomUp(x:str,y:str):
    ''' edit distance using bottom up approach '''
    dp = [[None for j in range(len(y)+1)] for i in range(len(x)+1)]
    
    for i in range(0,len(x)+1):
        dp[i][0] = i
    for j in range(0,len(y)+1):
        dp[0][j] = j
    
    for j in range(1,len(y)+1):
        for i in range(1,len(x)+1):
            dp[i][j] = min(diff(x,y,i-1,j-1)+dp[i-1][j-1],1+dp[i-1][j],1+dp[i][j-1])
    for i in dp:
        print(i)
    Align(x,y,dp)
    return dp[-1][-1]

def Align(x:str,y:str,dp):
    i,j = len(x),len(y)
    ll = []
    while i > 0 and j > 0:
        m = min(dp[i-1][j-1], dp[i-1][j],dp[i][j-1])
        if m == dp[i-1][j-1]:
            #print(x[i-1], y[j-1], diff(x,y,i-1,j-1)) #1-based inndex
            ll.append(str(x[i-1])+' '+str(y[j-1])+' '+str(diff(x,y,i-1,j-1)))
            i -= 1
            j -= 1
        elif m == dp[i][j-1]:
            #print('_', y[j-1], 1)
            ll.append('_'+' '+str(y[j-1])+' '+'1')
            j -= 1
        elif m == dp[i-1][j]:
            #print(x[i-1], '_', 1)
            ll.append(str(x[i-1])+' '+'_'+' '+'1')
            i -= 1
    while i > 0:
        #print(x[i-1], '_', 1)
        ll.append(str(x[i-1])+' '+'_'+' '+'1')
        i -= 1
    while j > 0:
        #print('_', y[j-1], 1)
        ll.append('_'+' '+str(y[j-1])+' '+'1')
        j -= 1
    ll.reverse()
    for i in ll:
        print(i)
        
def main():
    # x = input()
    # y = input()
    x = 'exponential'
    y = 'polynomial'
    print('TopDown: ', Edit(x,y))
    print('BottomUp: ', EditBottomUp(x,y))
if  __name__ == '__main__':
    main()