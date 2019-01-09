#!/usr/bin/python3

from mystack import Stack

def eval_postfix(s):
    """Evaluates the postfix expression 's'."""
    S = Stack()
    for ch in s:
    	if ch in ('+','-','*','/'):
            if S.isEmpty() is True:
                return "invalud expr"
            else:
                b = S.pop()
    		
            if S.isEmpty() is True:
                return "invalid expr"
            else:
                a = S.pop()
            res = expr(a,b,ch)
            S.push(res)
    	elif ch == ' ':
    		pass
    	else:
    		S.push(ch)
    ans = S.pop()

    if S.isEmpty() is False:
    	return "This is a false expr"
    return ans
def expr(a,b,op):
	if(op =='+'):
		return float(a)+float(b)
	if(op == '-'):
		return float(a)-float(b)
	if(op == '*'):
		return float(a) * float(b)
	if(op == '/'):
        #if(b == '0'):
        #    return -99
		return float(a)/float(b)

def main():
	expr = input('Enter the postfix expression: ').split()

	print('The value of the expression is',eval_postfix(expr))

if __name__ == '__main__':
    main()

