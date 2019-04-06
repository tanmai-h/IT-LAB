#Huffman encoding
import heapq

class Node:
    ''' freq, symbol, left, right '''
    def __init__(self,symbol=None,freq=0,left=None,right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, x):
        return self.freq < x.freq
def Huffman(tab):
    nodes = []
    for symb, freq in tab.items():
        x = Node(symb,freq)
        nodes.append(x)
    heapq.heapify(nodes)
    for i in range(len(tab)-1):
        t_1 = heapq.heappop(nodes)
        t_2 = heapq.heappop(nodes)
        x = Node(symbol=None,freq=t_1.freq+t_2.freq,left=t_1,right=t_2)
        heapq.heappush(nodes, x)
    
    return heapq.heappop(nodes)

def getEncoding(root):
    ''' returns a dict with encodings '''
    dict = {}
    str = ''
    _getEncoding(root, str, dict)
    
    return dict
def _getEncoding(root,str,dict):
    ''' places encodings into the dict '''
    if root.left == None or root.right == None:
        dict[root.symbol] = str
    else:
        _getEncoding(root.left,str+'0',dict)
        _getEncoding(root.right,str+'1',dict)

def EncodeFile(fileName):
    table = {}
    with open(fileName, 'r') as file:
        while True:
            ch = file.read(1)
            if not ch:
                break
            if ch in table:
                table[ch] += 1
            else:
                table[ch] = 0
    file.close()

    encodings = getEncoding(Huffman(table)) 
    compress = open('encoded.txt', 'w')
    
    with open(fileName, 'r') as original:
        while True:
            ch = original.read(1)
            if not ch:
                break
            code = encodings[ch]
            compress.write(code)
    original.close()
    compress.close()

    return encodings
def DecodeFile(fileName, encodings):
    reverse_encoding = {}
    decode = open('decoded.txt','w')
    for symbol, code in encodings.items():
        reverse_encoding[code] = symbol
    
    print(reverse_encoding)
    with open(fileName, 'r') as file:
        code = ''
        while True:
            ch = file.read(1)
            if not ch:
                break
            else:
                if code in reverse_encoding:
                    #print(code)
                    decode.write(reverse_encoding[code])
                    code = ''
                else:
                    code += ch
    decode.close()
    file.close()

def test():
    n = int(input('no. of symbols\n'))
    print('symbol freq')
    tab = {}
    for i in range(n):
        s,f = [x for x in input().strip().split()]
        tab[s] = int(f)
    
    Tree = Huffman(tab)
    encodings = getEncoding(Tree) 
    print(encodings)

    cost = 0
    for symbol, code in encodings.items():
        cost += len(code) * tab[symbol]
    print('Size of encoded file: ', cost, ' bits')

if __name__ == '__main__':
    # test()
    encodings = EncodeFile('sample.txt')
    print(encodings)
    print('\n\n')
    DecodeFile('encoded.txt', encodings)