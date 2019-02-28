# disjoint set

class DSJ:
    def __init__(self, s = 1):
        self.size = s
        self.parent = [None for i in range(s)]
        self.rank = [None for i in range(s)]
    
    def makeset(self, i):
        self.parent[i] = i
        self.rank[i] = 0
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        
        return self.parent[i]
    def union(self, u, v):
        ru = self.find(u)
        rv = self.find(v)
        if self.rank[ru] > self.rank[rv]:
            self.parent[rv] = ru
        elif self.rank[ru] < self.rank[rv]:
            self.parent[ru] = rv
        else:
            self.parent[rv] = ru
            self.rank[ru] += 1
    
    def __str__(self):
        s = ""
        for i in range(len(self.parent)):
            s += str(i) + " rank - " + str(self.rank[i]) + " -p  " + str(self.parent[i]) + '\n'
        return s     
        
if __name__ == '__main__':
    d = DSJ(7)
    for i in range(7):
        d.makeset(i)
    
    d.union(0,1)
    d.union(0,2)
    d.union(3,4)
    d.union(4,5)
    d.union(3,6)
    d.union(0,4)
    print(d)
    print(d.find(4))
    print(d.find(5))
    print(d.find(1))
    print(d.parent[5])