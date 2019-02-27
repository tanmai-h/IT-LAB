class Node:
    def __init__(self, val = None, parent = None):
        self.val = val
        self.left = self.right = None
        self.parent = parent

class BST:
    def __init__(self):
        self.root = None
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)
    def _insert(self, root, val):
        if root is None:
            root = Node(val)
        if  val < root.val:
            if root.left is None:
                root.left = Node(val, root)
            else:
                self._insert(root.left, val)
        elif  val > root.val :
            if root.right is None:
                root.right = Node(val, root)
            else:
                self._insert(root.right, val)
        else:
            return
        
    def delete(self, val):
        if self.root is not None:
            self._delete(self.root, val)
    def _delete(self, root, val):
        if not root:
            return
        elif val < root.val:
            root.left = self._delete(root.left, val)
        elif val > root.val:
            root.right = self._delete(root.right, val)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                nn = self.minNode(root.right)
                root.val = nn.val
                root.right = self._delete(root.right, nn.val)
            
        return root

    def minNode(self, root):
        temp = root
        while temp.left != None:
            temp = temp.left
        return temp
def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
pIndex = 0
def _construct(low, high, preorder):              
    global pIndex    
    if pIndex >= len(preorder) or low > high:
        return None
    else:        
        root = Node(preorder[pIndex])
        pIndex = pIndex + 1
        if low == high:
            return root
        for i in range(low, high+1):
            if preorder[i] > root.val:
                break
        root.left = _construct(pIndex, i-1, preorder)
        root.right = _construct(i, high, preorder)

        return root
def construct(preorder):
    
    return _construct(0, len(preorder)-1, preorder)

def part(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pi = part(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)  

class vertex:
    def __init__(self, val = None):
        self.val = val
        self.parent = None
        self.hIndex = None
        self.dist = 99999999
        self.list = {}
    def add(self, v, w =0):
        self.list[v] = w

class Graph:
    def __init__(self, V):
        self.verts = {}
        self.visited = {}
    def addEdge(self, u, v, w = 0):
        if u not in self.verts:
            self.verts[u] = vertex(u)
        if v not in self.verts:
            self.verts[v] = vertex(v)

        self.verts[u].add(v, w)

def Dijkstra(G, s):
    G.verts[s].dist = 0
    for u in G.verts:
        H.insert(G.verts[u])
    H.buildHeap()

    while H.isEmpty() != True:
        u = H.extractMin()
        for v in u.list:
            vv = G.verts[v]
            if vv.dist > u.dist + u.list[v]
                vv.dist = u.dist + u.list[v]
                H.updatePr(vv)
                vv.parent = u
def main():
    #T = BST()
    pre = [10, 5, 1,7, 40, 50]
    ino = sorted(pre)
    dict = {x: y for (x,y) in enumerate(pre)}
    #print(dict)
    root = construct(pre)
    inorder(root)
    print()
    T = BST()
    T.root = root
    T.delete(40)
    T.delete(10)
    inorder(root)
    quicksort(pre, 0, len(pre)-1)
    print()
    #print(pre)
if __name__ == '__main__':
    main()