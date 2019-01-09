#Hash Table
from linked_list import LinkedList
SIZE = 113
class HashTable:
	def __init__(self):
		self.T = [LinkedList() for i in range(SIZE)]

	def insert(self, element, flag = 0):
		if(self.search(element) == True):
			return
		else:
			if flag == 0:
				index = self.findHash(element)
			else:
				index = self.findHashHorner(element)

		self.T[index].insert(element, self.T[index].head)
		
	def insertHorner(self, element):
		index = self.findHashHorner(element)
		self.T[index].insert(element, self.T[index].head)
	
	def findHashHorner(self, string, x = 33): 
		n = len(string)
		result = ord(string[0])
		for i in range(1, n): 
			result = result*x + ord(string[i])
		return result%SIZE 

	def findHash(self, element):
		x = 0
		for i in element:
			x += ord(i)
		return x % SIZE

	def keys(self):
		i = 0
		for chain in self.T:
			l = chain.print()
			if len(l) is not 0:
				print(str(i) + " - ", end=" ")
				print(l)
			i = i+1

	def search(self, element, flag = 0):
		if flag == 1:
			index = self.findHashHorner(element)
		else:
			index = self.findHash(element)

		return self.T[index].search(element)

def buildFromFile(table, fName):
	with open(fName, 'r') as file:
		while file:
			word = file.readline()
			if not word:
				break
			else:
				word = word[:-1]
				table.insertHorner(word)
def main():
	w = HashTable() 
	w.insert("catcat")
	w.insert("qwp0nsd")
	w.insert("qsd")
	w.insert("q213")
	w.insert("act")
	w.insert("tac")
	w.insert("cat")
	w.insert("abc")
	w.insert("adc")
	w.keys()
	st = input("Enter search word: ")
	if w.search(st) == True:
		print("Found")
	else:
		print("Not Found")
if __name__ == '__main__':
    main()