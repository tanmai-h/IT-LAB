from collections import defaultdict 
from math import inf

class Graph:   
    def __init__(self,vertices): 
        self.V = vertices 
        self.graph = [] 
   
    def addEdge(self,u,v,w): 
        self.graph.append([u, v, w]) 
          
    def printDist(self, dist): 
        print("Vertex   Distance from Source") 
        for i in range(self.V): 
            print("%d \t\t %d" % (i, dist[i])) 
      
    def BellmanFord(self, src): 
        dist = [inf] * self.V 
        dist[src] = 0 
        for i in range(self.V - 1): 
            for u, v, w in self.graph: 
                if dist[u] != inf and dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w 
  
        for u, v, w in self.graph: 
            if dist[u] != inf and dist[u] + w < dist[v]: 
                print("Graph contains negative weight cycle!")
                    return
        self.printDist(dist) 
  
def main():  
    g = Graph(8) 
    g.addEdge(1,0,1) 
    g.addEdge(1,2,1) 
    g.addEdge(2,3,3) 
    g.addEdge(3,4,-1) 
    g.addEdge(5,4,-1) 
    g.addEdge(6,5,1) 
    g.addEdge(7,6,8) 
    g.addEdge(7,0,10) 
    g.addEdge(5,0,-4)
    g.addEdge(0,4,2)  
    g.addEdge(4,1,-2)  
    g.BellmanFord(7) 

if __name__ == '__main__':
    main()