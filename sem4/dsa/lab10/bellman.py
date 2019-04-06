#Bellman - Ford for shortest paths
from math import inf

def BellmanFord(G, source):
    ''' Use bottom approach '''	
    n = len(G)
    prev = [None for i in range(n)]
    DistTable = [[inf for _ in range(n)] for _ in range(n)] #dist[source][v] = inf
    for k in range(n):
        DistTable[source][k] = 0

    dd = {0:'s',1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g'}
    for k in range(1,n):
        for u in range(n):
            for v,w in G[u]:
                DistTable[v][k] = min(DistTable[u][k-1]+w, DistTable[v][k])
                if DistTable[v][k] == DistTable[u][k-1]+w:
                    prev[v] = u
    for u in range(n):
        for v,w in G[u]:
            if DistTable[v][-1] != inf and DistTable[v][-1] > DistTable[u][-1]+w:
                print('Graph has negative cycle')
                return
    for i in range(n):
        path(i,prev, dd)
        print()
    ########### Pretty Print####:
    
    print('   ',end='')
    for k in range(n):
        print("%5d"%(k),end='')
    print()
    for u in range(n):
        print("%1s  "%(dd[u]),end='')
        for i in DistTable[u]:
            print("%5s"%(str(i)),end='')
        print()
    #################  
def path(i, prev, dd):
    if prev[i] != None:
        path(prev[i],prev,dd)
    print(dd[i], end = ', ')
def main():
    v,e = [int(x) for x in input().split()]
    Graph = [[] for _ in range(v)]

    for _ in range(e):
        u,v,w = [int(x) for x in input().split()]
        Graph[u].append((v,w))
    
    BellmanFord(Graph, source=0)
if __name__ == '__main__':
    main()