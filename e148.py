import math
#assume p prime
#returns the number of entries in the first n rows of Pascal's triangle NOT divisible by p 
def pascal_divs(n,p):
  if n == 0:
    return 0
  if n <= p:
    return n*(n+1)/2
  #if n == p^k, we get (p*(p+1)/2)^k
  #compute closest power of p less than n
  pPow = int(math.floor(math.log(n)/math.log(p)))
  row = n / (p**pPow)
  rem = n % (p**pPow)
  return (row*(row+1))/2*(p*(p+1)/2)**pPow + (row+1) * pascal_divs(rem,p)

print pascal_divs(10**9,7)
