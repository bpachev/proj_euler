from fractions import gcd

def isqrt(n):
	return int(n**.5)

def get_continued_fraction(n):
	"""Find the continued fraction representation of a number n
	"""
	MAX_ITERS = 10**5
	orig_m = isqrt(n)
	a = 1 #Coefficient by the square root
	b = 0 #bias term in numerator
	c = 1 #integer denominator
	parts = []
	if orig_m**2 == n: return [orig_m], None
	root = n**.5

	seen_tuples = {}

	for i in range(MAX_ITERS):
		#Given a fraction in the form [a*sqrt(n) + b] / c
		#Get the whole part
		m = int((a*root+b)/c)
		seen_tuples[(a,b,c)] = i
		parts.append(m)
		#Now, we write [a*sqrt(n) + b] / c = m + 1/x
		#Hence, x = c / (a*sqrt(n) + b - c*m) (after simplifying)
		#Then, we multiply the numerator and denominator by a*sqrt(n) - b + c*m, which gives
		new_a, new_b, new_c = c*a, c*(c*m-b), a**2*n - (c*m - b) ** 2
		d = gcd(gcd(new_a, new_b), new_c)
		a, b, c = new_a // d, new_b // d, new_c // d
		k = (a,b,c)

		if k in seen_tuples:
			print("Terminating computation, cycle found.")
			period_start = seen_tuples[k]
			return parts, period_start

	raise ValueError("Period greater than "+str(MAX_ITERS))

print(get_continued_fraction(94))
