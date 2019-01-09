#SpellChreck
from hashTable import HashTable

def buildFromFile(hashTable, fName):
	with open(fName, 'r') as file:
		while file:
			word = file.readline()
			if not word:
				break
			else:
				word = word[:-1]
				hashTable.insert(str(word), 1)
def main():
	t = HashTable()
	buildFromFile(t, 'small.dict')
	#t.keys()
	ans = t.search(input("enter word to search for: "), 1)
	if(ans == True):
		print("valid word")
	else:
		print("invalid word")
if __name__ == '__main__':	
    main()
