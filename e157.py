from proj_euler import shanks_factorize

def count_divs(factors):
 print factors
 res = 1
 for f in factors:
  res *= factors[f]+1
 return res

def num_sols(n):
 """
 Counts all solutions to the diophantine equation 1/a+1/b=p/10^k for 1<=k<=n
 All variables are positive integers.
 """
 tot = 0
 cur = 1
 for k in xrange(1,n+1):
  
  #We must have that a and b are of the form k*2^e1*5^e2, where k is the same for both a and b
  #The maximum power of 2 present must equal the maximum power of 5 present
  #loop over smaller
  pow5 = [5**i for i in xrange(n+2)]
  pow2 = [2**i for i in xrange(n+2)] 
  for small5 in xrange(k+1):
   for small2 in xrange(k+1):
    cur+=count_divs(shanks_factorize(pow5[k-small5]*pow2[k-small2] + 1))
    cur+=count_divs(shanks_factorize(pow5[k-small5] + pow2[k-small2]))
  tot += (n-k+1)*cur
 return tot
print num_sols(1)
    
