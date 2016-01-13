import this

def Fib(n):
	a, b, p, q = 1, 0, 0, 1
	while True:
		if n == 0:
			break
		elif n & 1 == 0:
			a, b, p, q, n = a, b, p * p + q * q, 2 * p * q + q * q, n >> 1
		else:
			a, b, p, q, n = b * q + a * q + a *p, b * p + a * q, p , q, n - 1
	return b
c=map(Fib,range(10))
print c