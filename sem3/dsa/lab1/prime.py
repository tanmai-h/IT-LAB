import math as M

def prime(p):
	for i in range(2, int(M.sqrt(p)+1)):
		if p%i == 0:
			return "Not prime"
	return "Prime"

print(prime(int(input("Enter num: "))))