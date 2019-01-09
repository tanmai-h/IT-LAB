from graph import Graph
from queue import Queue

def BFS(G, source):
    Q = Queue(1000)
    Q.push(source)
    G.visited[source] = 1
    G.dist[source] = 0
    #print("BFS traversal: ", end = " ")
    while (Q.isEmpty() is False):
        t = Q.peek()
        print(t, end = " ")
        Q.pop()
        for i in G.adjList[t]:
            if G.visited[i] == 0:
                Q.push(i)
                G.visited[i] = 1
                G.dist[i] = G.dist[t] + 1
    print()
   
def main():
    v = int(input("num vertices: "))
    G = Graph(v) 
    print("enter edges")
    G.input()

    source = int(input("Source vertex: "))    
    BFS(G, source)
    
    print("dist of vertex i from ", source)
    for i in range(0, G.V):
        print(i, ": ", G.dist[i])
        
if __name__ == '__main__':
    main()