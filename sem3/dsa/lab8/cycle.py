from graph import Graph

def DFS(G, u, current):
    G.visited[u] = 1
    current[u] = 1
    
    for t in G.adjList[u]:
        if G.visited[t] == 0:
            DFS(G, t, current)
        elif current[t] == 1:
            return True
    current[u] = 0
    return False


def detectCycle(G):
    current = [None for i in range(G.V)]
    for i in range(G.V):
        if G.visited[i] == 0:
            c = DFS(G, i, current)
            if c == True:
                print("Cycle exists")
                return True
            else:
                print("No Cyle")
                return False
def main():
    v = int(input("num vertices: "))
    G = Graph(v) 
    print("enter edges")
    G.input()
    detectCycle(G)

if __name__ == '__main__':
    main()