class TreeNode:
    def __init__(self,key=None,parent=None):
        self.key=key
        self.left=None
        self.right=None
        self.parent=parent


class BSTree:
    def __init__(self,root=None):
        self.root=root

    def insert(self,key):
        if self.root is None:
            self.root=TreeNode()
            self.root.key=key
            return
        prev=temp=self.root
        while temp:
            if key<temp.key:
                prev=temp
                temp=temp.left
            else :
                prev=temp
                temp=temp.right
        if key < prev.key:
            prev.left=TreeNode(key,prev)
        else :
            prev.right=TreeNode(key,prev)

    def delete(self,node):
        if node is None:
            return
        p=node.parent
        if node.left==None and node.right==None :
            if p.left==node:
                p.left=None
            else :
                p.right=None
            node.key=node.parent=None
        elif node.left==None :
            node.right.parent=p
            if p.left==node:
                p.left=node.right
            else :
                p.right=node.right
            node.key=node.parent=None
        elif node.right==None:
            node.left.parent=p
            if p.left is node:
                p.left=node.left
            else :
                p.right=node.left
            node.key=node.parent=None
        else :
            succ=self.successor(node)
            k=succ.key
            self.delete(succ);
            succ.left=node.left
            succ.right=node.right
            succ.parent=p
            if p.left==node:
                p.left=succ
            else :
                p.right=succ
            node.left=node.right=node.key=node.parent=None
            succ.key=k


    def search(self,key):
        temp=self.root
        while temp:
            if key == temp.key :
                return True
            elif key < temp.key:
                temp=temp.left
            else :
                temp=temp.right
        return False

    def successor(self,node):

        if node.right:
            temp=node.right
            while temp.left:
                temp=temp.left
            return temp
        else :
            prev=node
            temp=node.parent
            while temp:
                if temp.left==prev:
                    break
                prev=temp
                temp=temp.parent
            return temp

    def predecessor(self,node):
        if node.left:
            temp=node.left
            while temp.right:
                temp=temp.right
            return temp
        else :
            prev=node
            temp=node.parent
            while temp:
                if temp.right==prev:
                    break
                prev=temp
                temp=temp.parent
            return temp

    def traverse(self,type='IN'):
        if self.root is None:
            return
        if type is 'IN':
            self.__inOrder(self.root)
        elif type is 'PRE':
            self.__preOrder(self.root)
        elif type is 'POST':
            self.__postOrder(self.root)
        else :
            self.__inOrder(self.root)
        print()
    
    def __inOrder(self,node):
        if node.left:
            self.__inOrder(node.left)
        print(node.key,end=' ')
        if node.right:
            self.__inOrder(node.right)
    
    def __preOrder(self,node):
        print(node.key,end=' ')
        if node.left:
            self.__preOrder(node.left)
        if node.right:
            self.__preOrder(node.right)

    def __postOrder(self,node):
        if node.left:
            self.__postOrder(node.left)
        if node.right:
            self.__postOrder(node.right)
        print(node.key,end=' ')

    def maximum(self):
        temp=self.root
        while temp and temp.right:
            temp=temp.right
        return temp

    def minimum(self):
        temp=self.root
        while temp and temp.left:
            temp=temp.left
        return temp

def test():
    b=BSTree()
    b.insert(5)
    b.insert(1)
    b.insert(6)
    b.insert(4)
    b.insert(0)
    b.insert(7)
    b.traverse()
    b.delete(b.root.left)
    b.traverse()
if __name__=='__main__':
    test()

        


    