def fib(n):
	l = [0, 1]
	a = 0
	b = 1
	for i in range(n-2):
		c = a+b
		a = b
		b = c
		l.append(c)
	return l
print(fib(int(input("enter n: "))))