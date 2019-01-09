from hashTable import HashTable
from spell import buildFromFile

def getWordList(word):
    list = []
    for i in range (0, len(word)):
        for j in range(0, 26):
            splice = word[:i] + chr(j + ord('a')) + word[i+1:]
            list.append(splice)
    return list
def main():
    table = HashTable()
    buildFromFile(table, 'ispell.dict')
    print("dictionary built.")
    
    while True:
        word = input("word: ")
        if (table.search(word, 1) == True):
            print("Word found")
        else:
            list = getWordList(word)
            print("Suggestions:  ", end = "")
            for w in list:
                if (table.search(w, 1) == True):
                    print(w, end = " ")
            print("\n")
if __name__ == '__main__':	
    main()
