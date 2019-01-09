from mystack import Stack

def find(a,b,op):
	if(op == '+'):
		return int(a)+int(b)
	if(op=='-'):
		return int(a)-int(b)
	if(op=='*'):
		return int(a) * int(b)
	if(op=='/'):
		return int(a)/int(b)

def eval_prefix(expr):
	s = Stack()
	for i in range(len(expr)-1, -1, -1):
		ch = expr[i]

		if ch in ('+','-','*','/'):
			if s.isEmpty() is True:
				return "invalid expr"
			else:
				b = s.pop()
			if s.isEmpty() is True:
				return "invalid expr"
			else:
				a = s.pop()
			res = find(b,a,ch)
			s.push(res)
		
		elif ch == ' ':
			pass
		else:
			s.push(ch)
	ans = s.pop()

	if s.isEmpty() is False:
		return "This is a false expr"
	return ans


def main():
	expr = input('Enter the prefix expression: ').split()

	print('The value of the expression is',eval_prefix(expr))

if __name__ == '__main__':
    main()
