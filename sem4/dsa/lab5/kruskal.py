# kruskal
from dsj import DSJ

class Graph:
    def __init__(self, V=0, E=0):
        self.adj = [[] for i in range(V)]
        self.weight = [{} for i in range(V)]
        self.V = V
        self.E = E

    def add(self, u, v, w=0, undirected = True):
        self.adj[u].append(v)
        self.weight[u][v] = w

        if undirected == True:
            self.adj[v].append(u)
            self.weight[v][u] = w       
        
def kruskal(G):
    edges,T = [],[]
    cost = 0

    dsj = DSJ(G.V)

    for u in range(G.V):
        for v in G.adj[u]:
            edges.append((u,v))
    edges = sorted(edges,key=lambda pair: G.weight[pair[0]][pair[1]])
    edges.reverse()
    
    for i in range(G.V):
        dsj.makeset(i)
    
    while len(T) < G.V - 1:
        u,v = edges.pop()
        if dsj.find(u) != dsj.find(v):
            dsj.union(u,v)
            T.append((u,v))
            cost += G.weight[u][v]
    return T,cost

def G_input():
    V,E = [int(x) for x in input().strip().split()]
    G = Graph(V,E)
    for i in range(E):
        x,y,w = [int(i) for i in input().split()]
        G.add(x,y,w)
    
    return G

if __name__ == '__main__':
    G = G_input()
    
    T = kruskal(G)
    print(T)