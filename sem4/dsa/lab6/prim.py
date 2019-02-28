from minheap import MinHeap

class Graph:
    def __init__(self, V=0, E=0):
        self.adj = [[] for i in range(V)]
        self.weight = [{} for i in range(V)]
        self.prev = [None for i in range(V)]
        self.cost = [1e5 for i in range(V)]
        self.V = V
        self.E = E

    def add(self, u, v, w=0, undirected = True):
        self.adj[u].append(v)
        self.weight[u][v] = w

        if undirected == True:
            self.adj[v].append(u)
            self.weight[v][u] = w   

def prim(G):
    H = MinHeap(lambda x:G.cost[x])
    G.cost[0] = 0
    H.buildHeap([i for i in range(G.V)])

    while H.size > 0:
        u = H.extractMin()
        for v in G.adj[u]:
            if G.cost[v] > G.weight[u][v]:
                G.cost[v] = G.weight[u][v]
                G.prev[v] = u
                H.buildHeap([i for i in range(G.V)])
    T = []
    for i in range(G.V):
        if G.prev[i] is not None:
            T.append((G.prev[i],i))
    
    return T
def G_input():
    V,E = [int(x) for x in input().strip().split()]
    G = Graph(V,E)
    for i in range(E):
        x,y,w = [int(i) for i in input().split()]
        G.add(x,y,w)
    
    return G

if __name__ == '__main__':
    G = G_input()
    
    T = prim(G)
    print(T)