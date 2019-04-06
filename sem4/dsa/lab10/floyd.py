from math import inf

def floyd(G):
    n = len(G)
    dist = [[[inf for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v,w in G[u]:
            dist[u][v][0] = w
    for u in range(n):
        for k in range(n):
            dist[u][u][k] = 0
            
    for k in range(1,n):
        for i in range(n):
            for j in range(n):
                dist[i][j][k] = min(dist[i][k][k-1] + dist[k][j][k-1], dist[i][j][k-1])
    
    dd = {0:'s',1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g'}
    
    ########### Pretty Print####:
    print('   ',end='')
    for i in range(n):
        print("%5s"%(dd[i]),end='')
    print()
    for i in range(n):
        print("%1s  "%(dd[i]),end='')
        for j in range(n):
            print("%5s"%(str(dist[i][j][n-1])),end='')
        print()
    #################  

def main():
    v,e = [int(x) for x in input().split()]
    Graph = [[] for _ in range(v)]

    for _ in range(e):
        u,v,w = [int(x) for x in input().split()]
        Graph[u].append((v,w))
    
    floyd(Graph)
if __name__ == '__main__':
    main()