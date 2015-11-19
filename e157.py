from proj_euler import shanks_factorize

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
  for small5 in xrange(
 
