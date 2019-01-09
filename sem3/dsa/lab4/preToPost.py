from mystack import Stack

def isOperator(c):
	if c in ('+', '-', '*', '/'):
		return True
	return False

def convert(expr):
	post = ""
	s = Stack()
	for i in range(len(expr)-1, -1, -1):
		if isOperator(expr[i]) is True:
			#print(expr[i])
			if s.isEmpty() is True:
				return "invalid expr"
			else:
				post += s.pop()
			if s.isEmpty() is True:
				return "invalid expr"
			else:
				post += s.pop()
			post += expr[i]
			s.push(post)
			#print(s.topE())
			post = ""
		elif expr[i] is " ":
			pass
		else:
			s.push(expr[i])
			#print(s.topE())
	return s.topE()

expr = input('Enter the prefix expression: ')
print(convert(expr))