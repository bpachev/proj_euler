from itertools import permutations, combinations,product
from proj_euler import mark_primes, MillerRabin 
from math import factorial

n = 9
maxDivs = n/2+1
cap = 10**6
mask = mark_primes(cap)

def is_prime(n):
	global mask,cap
	if n <= cap:
		return mask[n]
	else:
		return MillerRabin(n)

def is_good(p,c):
	num = 0
	for i,d in enumerate(p):
		num *= 10
		num += d
		if i in c:
			if not is_prime(num):
				return 0
			num=0
	if not is_prime(num):
		return 0
	return 1

print is_good([2,5,4,7,8,9,6,3,1],(0,1,3,5))

cutoffs = []
s = {k:0 for k in xrange(1,maxDivs+2)}
for i in xrange(1,max(maxDivs+1,2)):
  cutoffs = cutoffs + list(combinations(range(n-1),i))

i = 0
for p in permutations(range(1,n+1)):
  for c in cutoffs:
   l = len(c)+1
   if is_good(p,c):
     s[l] += 1
#     print p
#     print c
print s
print sum([s[i]/factorial(i) for i in s])