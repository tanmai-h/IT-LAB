class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
class AVL:
    def insert(self, root, val):
        if not root:
            return TreeNode(val) 
        elif val <= root.val: 
            root.left = self.insert(root.left, val) 
            root.left.parent = root
        elif val > root.val: 
            root.right = self.insert(root.right, val) 
            root.right.parent = root
        #else:
        #    return root
        #update height
        root.height = 1 + max(self.getH(root.left), self.getH(root.right))

        balance = self.getBalance(root)

        if balance > 1:
            if val < root.left.val: #left-left
               return self.RightRotate(root)
            elif val > root.left.val: #left-right
                root.left = self.LeftRotate(root.left)
                return self.RightRotate(root)
        elif balance < -1:
            if val > root.right.val: #right-right
                root = self.LeftRotate(root)
            elif val < root.right.val: #right-left
                root.right = self.RightRotate(root.right)
                return self.LeftRotate(root)
        
        return root
    
    def delete(self, root, val): 
        #normal bst del 
        if not root: 
            return root  
        elif val < root.val: 
            root.left = self.delete(root.left, val) 
        elif val > root.val: 
            root.right = self.delete(root.right, val) 
        else:                       #node to delete
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
                
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.getMin(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right, 
                                      temp.val) 
        if root is None: 
            return root 

        root.height = 1 + max(self.getH(root.left), 
                            self.getH(root.right)) 
  
        balance = self.getBalance(root)
  
        if balance > 1: 
            if self.getBalance(root.left) >= 0: #left-left
                return self.RightRotate(root) 
            if self.getBalance(root.left) < 0: #left - right
                root.left = self.LeftRotate(root.left) 
                return self.RightRotate(root) 

        if balance < -1: 
            if self.getBalance(root.right) <= 0: #right-right
                return self.LeftRotate(root) 
            if self.getBalance(root.right) > 0: #right-left
                root.right = self.RightRotate(root.right) 
                return self.LeftRotate(root) 
        return root  
    def RightRotate(self, root):
        newRoot = root.left
        z = newRoot.right
        
        root.left = z
        newRoot.right = root

        root.height = 1 + max(self.getH(root.left), self.getH(root.right))
        newRoot.height = 1 + max(self.getH(newRoot.left), self.getH(newRoot.right))

        return newRoot

    def LeftRotate(self, root):
        newRoot = root.right
        z = newRoot.left
        
        root.right = z
        newRoot.left = root

        root.height = 1 + max(self.getH(root.left), self.getH(root.right))
        newRoot.height = 1 + max(self.getH(newRoot.left), self.getH(newRoot.right))

        return newRoot
    
    def search(self,root,key):
        if(root == None):
            return False
            #print("It does not exist")
        elif(root.val<key):
            root = root.right
            return self.search(root,key)
        elif(root.val > key):
            root=root.left
            return self.search(root,key)
        elif(root.val==key):
            #print("It exists")
            
            return root
    def successor(self,root,key):
        key = self.search(root,key)
        if key == False:
            print("No successor")
        if key.right is not None:
            return self.minimum(key.right)
        else:
            y = key.parent
            print(y)
            while y is not None and key==y.right:
                 key = y
                 y = y.parent
            return y
    
    def predecessor(self, root, key):
        key=self.search(root,key)
        if key == False:
            print("No pred")
        if key.left is not None:
            return self.maximum(key.left)
        else:
            y = key.parent
            while y is not None and key==y.left:
                key = y
                y = y.parent
            return y
    def maximum(self,root):
        while root.right is not None:
            root=root.right
        return root

    def minimum(self,root):
        while root.left is not None:
            root=root.left
        return root
    def getMin(self, root): 
        if root is None or root.left is None: 
            return root 
  
        return self.getMin(root.left)
    
    def getH(self, root):
        if root is None:
            return 0
        else:
            return root.height
    def getBalance(self, root):
        return self.getH(root.left) - self.getH(root.right)
    def preOrder(self, root): 
        if not root: 
            return
        print(root.val, end = " ")
        self.preOrder(root.left) 
        self.preOrder(root.right) 

def main():
    T = AVL()
    root = None
    nums = [8,6,10,5,7]
    for i in nums:
        root = T.insert(root, i)
    T.preOrder(root)
    print()
    root = T.insert(root, 3)
    T.preOrder(root)
    print()
    root = T.insert(root, 4)
    T.preOrder(root)
    print()
    root = T.insert(root, 6)
    #T.preOrder(root)
    #print()
    
    print()
    root = T.delete(root, 7) 
    T.preOrder(root)
    print()
    root = T.delete(root, 10) 
    T.preOrder(root)
    print()
    
    #key = 6
    #print(T.successor(root,key).val)
    #root = T.insert(root, 10)
    #root = T.insert(root, 20) 
    #T.preOrder(root)
    #print()
    #root = T.insert(root, 30) 
    #T.preOrder(root)
    #print()
    #root = T.insert(root, 40) 
    #T.preOrder(root)
    #print()
    #root = T.insert(root, 50) 
    #T.preOrder(root)
    #print()
    #root = T.insert(root, 25)
    #T.preOrder(root)
    #print()

main()