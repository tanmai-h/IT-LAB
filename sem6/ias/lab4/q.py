import sys
import random
import hashlib

def ExtendedEuclid(a, b):
	s, old_s = 0, 1
	t, old_t = 1, 0
	r, old_r = b, a
	while r != 0:
		quotient = old_r // r
		old_r, r = r, old_r - quotient * r
		old_s, s = s, old_s - quotient * s
		old_t, t = t, old_t - quotient * t
	return old_r, old_s, old_t

def InverseModulo(n, p):
	gcd, x, y = ExtendedEuclid(n, p)
	assert (n * x + p * y) % p == gcd
	if gcd != 1:
		# Either n is 0, or p is not a prime number.
		raise ValueError(
			'{} has no multiplicative inverse '
			'modulo {}'.format(n, p))
	else:
		return x % p

def pickg(p):
	for x in range (1,p):
		rand = x
		exp=1
		next = rand % p

		while (next != 1 ):
			next = (next*rand) % p
			exp = exp+1

		if (exp==p-1):
			return rand


P, Q = 467, 497
r, s, c = 1111, 111, 1
g = 3
N = P * Q

g = 3
y = pow(g, s, N)
t = pow(g, r, N)

new_random = (r - c * s)

if (r < 0):
	Result = ( InverseModulo`(pow(g, -new_random, N), N) * pow(y, c, N) )  % N
else:
	Result = ( pow(g, new_random, N) * pow(y, c, N))  % N

print( '======Agreed parameters============')
print( 'P=',N, '\t(Prime number)')
print( 'G=',g, '\t(Generator)')
print( '======The secret==================')
print( 'x=',s,'\t(Alice\'s secret)')
print( '======Random values===============')
print( 'c=',c,'\t(Bob\'s random value)')
print( 'v=',r,'\t(Alice\'s random value)')
print( '======Shared value===============')
print( 'g^x mod P=\t',y)
print( 'r=\t\t',r)
print( '=========Results===================')
print( 't=g**v % n =\t\t',t)
print( '( (g**r) * (y**c) )=\t', Result)

if (t == Result):
	print( 'Alice has proven she knows password')
else:
	print( 'Alice has not proven she knows x')