import math
from MinHeap import MinHeap

class Vertex:
	def __init__(self,name):
		self.name=name
		self.neighbours={}
		self.ds = math.inf   				
		self.parent=None
		self.MHListIndex=None

	def Addneighbour(self,name,weight=0):
		self.neighbours[name]=weight

	def __str__(self):
		return str(self.name) + ' neighbours are ' + str([x for x in self.neighbours.keys()])

	def NeighbourWeight(self,nbr):
		if nbr in self.neighbours:
			return self.neighbours[nbr]

	def DistFromSource(self):
		return self.ds

	def __lt__(self,other):
		if self.ds < other.ds:
			return True
		elif self.ds > other.ds:
			return False

class Graph:
	def __init__(self):
		self.nv=0     
		self.Vertices={}    

	def AddVertex(self,name):
		self.nv=self.nv+1
		NewVertex=Vertex(name)
		self.Vertices[name]=NewVertex
		return NewVertex

	def AddEdge(self,Head,Tail,weight):   
		if Head not in self.Vertices:
			self.AddVertex(Head)
		if Tail not in self.Vertices:
			self.AddVertex(Tail)
		self.Vertices[Head].Addneighbour(Tail,weight)

	def GetVertex(self,name):
		if name in self.Vertices:
			return self.Vertices[name]

	def GetVertices(self):
		return self.Vertices.keys()

def Dijkstras(G,s,d):
	s.ds = 0
	Heap = MinHeap()
	for u in G.Vertices:
		Heap.Insert(G.Vertices[u])
	Heap.BuildHeap()
	while not Heap.isEmpty():
		U = Heap.ExtractMin()
		for v in U.neighbours:
			V = G.Vertices[v]
			if  V.DistFromSource() >= U.DistFromSource() + U.NeighbourWeight(v):
				V.ds = U.ds+U.NeighbourWeight(v)
				Heap.UpdatePriority(V)
				V.parent = U.name			

def PrintPath(G,d):                    
	if G.GetVertex(d).parent!=None:
		PrintPath(G,G.GetVertex(d).parent)
	print(G.GetVertex(d).name,',',end='')

def main():
	G=Graph()
	print("enter values")
	l=input()
	while l!='':
		l=l.split()
		G.AddEdge(l[0],l[1],int(l[2]))
		l=input()
	print("enter the source")
	s=input()
	for d in G.Vertices:
		if d!=s:
			Dijkstras(G,G.GetVertex(s),G.GetVertex(d))
			print("dest = ", d)
			PrintPath(G,d)
			print('dist: ', G.GetVertex(d).ds) 

if __name__=='__main__':
	main()
