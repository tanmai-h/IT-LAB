import bst as bst
def buildParseTree(expr):
    Tree = bst.BST()
    li=[]
    print(expr)
    for i in expr:
        if i is '(':
            li.append(bst.TreeNode(i))
        elif i is ')':
            right = bst.TreeNode(li.pop())
            mid = bst.TreeNode(li.pop())
            left = bst.TreeNode(li.pop())
            mid.left = left
            mid.right = right
            left.parent = right.parent = mid
            li.pop()
            li.append(mid)
        else :
            li.append(bst.TreeNode(i))
    
    t = bst.BST()
    t.root = li[0]
    return t

def calc(a,b,op):
    if(op=='+'):
        return a+b
    if(op=='-'):
        return a-b
    if(op=='*'):
        return a*b
    if(op=='/'):
        return a/b
    if(op=='^'):
        return a**b

def evalTree(parseTree):
    if parseTree.left is None:
        return int(parseTree.key)
    return calc(evalTree(parseTree.left),evalTree(parseTree.right),parseTree.key)



if __name__=='__main__':
    b=buildParseTree(input().split())
    print("Postfix : ",end='')
    b.traverse('postorder')
    
    print(b.root.left)
print(evalTree(b.root))