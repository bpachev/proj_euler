from proj_euler import shanks_factorize,divisors

def count_divs(factors):
 res = 1
 for f in factors:
  res *= factors[f]+1
 return res

def sols_for_one_pow(n):
 """
 Counts all solutions to the diophantine equation 1/a+1/b=p/10^n
 All variables are positive integers, n is fixed
 """
 tot = 0
 pow5 = [5**i for i in xrange(n+2)]
 pow2 = [2**i for i in xrange(n+2)] 
 for e1 in xrange(n+1):
  for e2 in xrange(n+1):
   a,b = pow5[e1],pow2[e2]
   mul = pow5[n-e1]*pow2[n-e2]
   tot += count_divs(shanks_factorize(mul*(a*b+1)))
   if e1 and e2:
    tot += count_divs(shanks_factorize(mul*(a+b)))
 return tot
 

def solve(n):
 """
 Counts all solutions to the diophantine equation 1/a+1/b=p/10^k for 1<=k<=n
 All variables are positive integers.
 """
 print "Solutions: %d" % sum([sols_for_one_pow(i) for i in xrange(1,n+1)])
solve(9)
    
