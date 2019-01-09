#BST Dict

class TreeNode:
    def __init__(self, key = None, value = None, parent = None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

class BST:
    def __init__(self):
        self.root = None
    def insert(self, key, value = "Null"):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self.insertHelper(key, value, self.root)

    def insertHelper(self, key, value, root):
        if  key < root.key:
            if root.left is None:
                root.left = TreeNode(key, value, root)
            else:
                self.insertHelper(key, value, root.left)
        elif  key > root.key :
            if root.right is None:
                root.right = TreeNode(key, value, root)
            else:
                self.insertHelper(key, value, root.right)
        else:
            return

    def search(self, key):
        return self.searchHelper(key, self.root)
    def searchHelper(self, key, root):
        if root is None:
            return None
        else:
            if key < root.key:
                return self.searchHelper(key, root.left)
            elif key > root.key:
                return self.searchHelper(key, root.right)
            else:
                return root
    def minimum(self, node):
        root = node
        if root is None:
            return None
        while root.left is not None:
            root = root.left
        return root
    def maximum(self, node):
        root = node
        if root is None:
            return None
        while root.right is not None:
            root = root.right
        return root

    def successor(self, key):
        t = self.search(key)
        if t is None:
            return False
        else:
            if t.right != None:
                return self.minimum(t.right)
            else:
                y = t.parent
                while(y != None and t == y.right):
                    t = y
                    y = t.parent
                if y == None:
                    return None
                else:
                    return y
    
    def predecessor(self, key):
        t = self.search(key)
        if t is None:
            return False
        else:
            if t.left != None:
                return self.maximum(t.left)
            else:
                y = t.parent
                while(y != None and t == y.left):
                    t = y
                    y = t.parent
                if y == None:
                    return None
                else:
                    return y
    
    def delete(self, key):
        if self == None:
            return
        node = self.search(key)
        self.remove(node)

    def remove(self, node):
        if node is None:
            return
        p = node.parent
        #print("parent = ", p.key)

        if node.left == None and node.right == None : #leaf
            if p == None:
                self.root = None
            else:
                if node == p.left:
                    p.left = None
                elif node == p.right:
                    p.right = None
        
        elif node.left == None :
            node.right.parent = p
            if p == None:
                self.root = node.right
            else:
                if p.left == node:
                    p.left = node.right
                else :
                    p.right=node.right
            node = None
            #node.key = node.parent = None
        
        elif node.right == None:
            node.left.parent = p
            if p == None:
                self.root = node.left
            else:
                if p.left == node:
                    p.left = node.left
                else :
                    p.right = node.left
            node = None
            #node.key=node.parent=None
        else:
            succ = self.successor(node.key)
            k = succ.key
            #print("succ parent ", succ.parent.key)
            self.remove(succ)
            succ.left = node.left
            succ.right = node.right
            succ.parent = p
            
            if p == None:
                self.root = succ
            else:
                if p.left == node:
                    p.left = succ
                else :
                    p.right = succ
            node.left = node.right = node.key = node.parent = None
            succ.key = k
    
    def traverse(self, method = "inorder"):
        if method == "postorder":
            self.postorder(self.root)
        elif method == "preorder":
            self.preorder(self.root)
        else:
            self.inorder(self.root)
        print()
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.key, end = " ")
            self.inorder(root.right)
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end = " ")
    def preorder(self, root):
        if root is not None:
            print(root.key, end = " ")
            self.preorder(root.left)
            self.preorder(root.right)
            
def main():
    Tree = BST()
    
    for i in range(0,10):
        Tree.insert(i)
    Tree.traverse()
    
    print(Tree.minimum(Tree.root).key)
    print(Tree.maximum(Tree.root).key)
    s = Tree.successor(int(input("succ: ")))
    if s is not None:
        print(s.key)
    else:
        print("No succ")
    
    p = Tree.predecessor(int(input("pred: ")))
    if p is not None:
        print(p.key)
    else:
        print("No pred")
    Tree.delete(4)
    Tree.traverse()
    #for i in range(0, 10):
    #    Tree.delete(i)
    #    Tree.traverse()

if __name__ == "__main__":
    main()
            