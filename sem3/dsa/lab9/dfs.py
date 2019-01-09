from graph import Graph

t = -1
def explore(G, u):
    global t
    G.visited[u] = 1
    print(u, end = " ")
    t = t + 1
    G.time[u][0] = t
    for v in G.adjList[u]:
        if G.visited[v] == 0:
            explore(G, v)
    t = t + 1
    G.time[u][1] = t

def DFS(G):
    s = int(input("Source: "))
    print()
    explore(G, s)
    #for i in range(G.V):
    #    if G.visited[i] == 0:
    #        explore(G, i)
    print()

def main():
    V = int(input("vertices: "))
    G = Graph(V)
    print("edges: ")
    G.input()

    DFS(G)

    for i in range(G.V):
        print(i, " [", G.time[i][0], ", ", G.time[i][1], "]")
if __name__ == '__main__':
    main()