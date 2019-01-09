def gcd(a, b):
	if(b == 0):
		return a
	else:
		if a < b:
			t = a
		else:
			t = b
		g  = 1
		for j in range (1, t+1):
			if a%j is 0 and b%j is 0:
				if j > g:
					g = j
		
		return g
x, y = [int(x) for x in input("enter 2 nos: ").split()]
print("gcd is ", gcd(x, y))