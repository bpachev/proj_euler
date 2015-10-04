cache = {}

def bin_steps(n):
  global cache
  if n in cache:
    return cache[n]
  
  if n <= 1:
    return float(n)
  
  temp = 1. + bin_steps(n-(n+1)/2)*((n-(n+1)/2)/float(n)) + bin_steps((n+1)/2-1)*(((n+1)/2-1.)/float(n))
  cache[n]=temp
  return temp
print bin_steps(10**10)
