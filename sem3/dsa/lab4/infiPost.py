#!/usr/bin/python3

from mystack import Stack

def Scale(ch):

	if(ch in ('*','/')):
		return 4
	if ch == '(':
		return -1
	return 3

def conInfi(expr):
	sc = Stack()
	pexp = ''
	for ch in expr:
		if ch in ('*','/','+','-'):
			while(sc.isEmpty() is False and Scale(sc.topE()) >= Scale(ch)):
				pexp += sc.pop()+ ' '
			sc.push(ch)
		elif ch == '(':
			sc.push(ch)
		elif ch == ')':
			while(sc.isEmpty() is False and sc.topE() is not '(' ):
				pexp+=sc.pop()
			sc.pop()
		else:
			pexp += ch+ ' '

	while(not sc.isEmpty()):
		pexp+=sc.pop()+' '
	return pexp

exp = input().split()
print(conInfi(exp))
