#Bellman - Ford for shortest paths
from math import inf
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

def G_input(undirected = True):
	V,E = [int(x) for x in input().strip().split()]
	G = Graph(V,E)
	for _ in range(E):
		x,y,w = [int(i) for i in input().split()]
		G.add(x,y,w,undirected=undirected)

	return G

def BellmanFord(G, source):
    ''' Use bottom approach '''	

    DistTable = [[inf for _ in range(G.V)] for _ in range(G.V)] #dist[source][v] = inf
    for k in range(G.V):
        DistTable[source][k] = 0

    dd = {0:'s',1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g'}
    for k in range(1,G.V):
        for u in range(G.V):
            for v in G.adj[u]:
                DistTable[v][k] = min(DistTable[u][k-1] + G.weight[u][v], DistTable[v][k])
            
    ########### Pretty Print####
    print('   ',end='')
    for k in range(G.V):
        print("%5d"%(k),end='')
    print()
    for u in range(G.V):
        print("%1s  "%(dd[u]),end='')
        for i in DistTable[u]:
            print("%5s"%(str(i)),end='')
        print()
    #################
def main():
    G = G_input(undirected=False)
    BellmanFord(G, source=0)
if __name__ == '__main__':
    main()