from mystack import Stack

def isMatched(expr):
    """Checks if the expression 'expr' has matching opening/closing symbols."""
    S = Stack()
    for ch in expr:
    	if ch in ('(', '[', '{'):
    		S.push(ch)
    	elif ch in ('}', ']', ')'):
    		if S.isEmpty():
    			return False
    		if matches(ch, S.topE()):
    			S.pop()
    		else:
    			return False
    	else:
    		pass
    if S.isEmpty():
    	return True
    return False
def matches(ch, S):
	if ch == ')' and S == '(' or ch ==']' and S == '['  or ch == '}' and S == '{':
		return True
	return False
def main():
	expr = input('Enter the expression: ')
	if isMatched(expr):
		print('Matched symbols')
	else:
		print('Unmatched symbols')

if __name__ == '__main__':
    main()

