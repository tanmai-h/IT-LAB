from graph import Graph
import bfs

def explore(G):
    print("components")
    for i in range(G.V):
        if G.visited[i] == 0:
            bfs.BFS(G, i)
        
def main():
    v = int(input("num vertices: "))
    G = Graph(v) 
    print("enter edges")
    G.input()
    print()

    explore(G)

if __name__ == '__main__':
    main()