def fact(f):
	if f < 0:
		return -1
	if f is 0:
		return 1
	f = 1
	for i in range(1, n+1):
		f = f*i
	return f
n = int(input("enter n: "))
print("n! = " , fact(n))