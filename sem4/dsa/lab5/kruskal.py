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
        
        if undirected == True:
            self.adj[v].append(u)

        self.weight[u][v] = w
        self.weight[v][u] = w
def MST(G):
    edges = []
    T = []
    dsj = DSJ(G.V)

    for u in range(G.V):
        for v in G.adj[u]:
            edges.append((u,v))
    
    edges = sorted(edges,key=lambda pair: G.weight[pair[0]][pair[1]])
    
    for i in range(G.V):
        dsj.makeset(i)
    
    for (u,v) in edges:
        if dsj.find(u) != dsj.find(v):
            dsj.union(u,v)
            T.append((u,v,G.weight[u][v]))

    print(T)
if __name__ == '__main__':
    V,E = [int(x) for x in input().strip().split()]
    G = Graph(V,E)
    for i in range(E):
        x,y,w = [int(i) for i in input().split()]
        G.add(x,y,w)
    print(G.weight[0][1])
    MST(G)