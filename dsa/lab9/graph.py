#print adj matrix and list

class Graph:
    def __init__(self, V = 0, E = 0):
        self.V = V
        self.E = E
        self.matrix = [[0] * V for i in range(0,V)]
        self.adjList = [[] for i in range(0,V)]
        self.visited = [0 for i in range(self.V)]
        self.dist = [-1 for i in range(self.V)]
        self.weight = [[]]
        self.time = [[-1,-1] for i in range(self.V)]

    def insert(self, x, y, w = -1, directed = 0):
        
        if w != -1:
            vertex = (y, w)
            self.adjList[x].append(vertex)

        else:
            self.adjList[x].append(y)
            if directed == 0:
                self.adjList[y].append(x)

            self.matrix[x][y] = 1
            if directed == 0:
                self.matrix[y][x] = 1
    
    def printMatrix(self):
        for i in range (0, self.V):
            for j in range(0, self.V):
                print(self.matrix[i][j], end = " ")
            print()
    def printList(self):
        for i in range(0, self.V):
            print(i, end = ": ")
            for j in range(0, len(self.adjList[i])):
                print(self.adjList[i][j], end = " ")
            print()
    def input(self):
        while True:
            q = input()
            if q.strip() == "":
                break
            else:
                x, y = [int(j) for j in q.split()]
                self.insert(x, y)
                self.E = self.E + 1

def main():
    v = int(input("num vertices: "))
    G = Graph(v) 
    print("enter edges")
    G.input()
    G.printList()
    print()
    G.printMatrix()

if __name__ == '__main__':
    main()