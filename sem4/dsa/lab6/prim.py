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
    H = MinHeap()
    G.cost[0] = 0
    G.cost[1] = 21
    G.cost[3] = 1
    H.buildHeap([i for i in range(G.V)])
    print(H.extractMin())
    print(H.extractMin())
    print(H.extractMin())
    # while H.size > 0:
    #     u = H.extractMin()
    #     print("min: ", u,end=": ")
    #     for v in G.adj[u]:
    #         if G.cost[v] > G.weight[u][v]:
    #             print(v, end=", ")
    #             G.prev[v] = u
    #             G.cost[v] = G.weight[u][v]
    #             #H.updatePriority(v)
    #             print('\n',H.heap)
    #             H.buildHeap([i for i in range(G.V)])
    #     print()
    # T = []
    # for i in range(G.V):
    #     if G.prev[i] is not None:
    #         T.append((G.prev[i],i))
    
    # return T

def G_input():
    V,E = [int(x) for x in input().strip().split()]
    G = Graph(V,E)
    for i in range(E):
        x,y,w = [int(i) for i in input().split()]
        G.add(x,y,w)
    
    return G

if __name__ == '__main__':
    G = G_input()
    '''
        7 11
        0 1 7
        0 3 5
        1 2 8
        1 3 9
        1 4 7
        2 4 5
        3 4 15
        3 5 6
        4 5 8
        4 6 11
        5 6 11
    '''
    T = prim(G)
    print(T)