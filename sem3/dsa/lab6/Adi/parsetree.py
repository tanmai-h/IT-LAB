import bst
def buildParseTree(expr):
    li=[]
    for i in expr:
        if i is '(':
            li.append(i)
        elif i is ')':
            right=li.pop()
            mid=li.pop()
            left=li.pop()
            mid.left=left
            mid.right=right
            left.parent=right.parent=mid
            li.pop()
            li.append(mid)
        else :
            li.append(bst.TreeNode(i))
    
    return bst.BSTree(li[0])

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
    b.traverse('POST')
    print("Prefix : ",end='')
    b.traverse('PRE')
    print(evalTree(b.root))
        