from bisect import bisect_left
fib = [0,1]
cap = 10**18
while fib[-1]<=cap:
  fib.append(fib[-1]+fib[-2])
  
def fib_floor(n):
  pos = bisect_left(fib,n)
  return fib[pos] if fib[pos] == n else fib[pos-1]
  

cache = {}
def G(n):
 return (n*(n+1)) / 2

def S(n):
  if n in cache:
    return cache[n]
  if n <= 0 or n == 1 or n == 2 or n == 3:
    return 0
  f = fib_floor(n)
  if n == f:
    cache[n] = S(n-1)
  else:
    thresh = (f-1)/2 #the maximum number of stones we can take, end at f, and not lose
    if n > f + thresh:
     cache[n] = S(f) + S(n-f) - S(thresh) + G(thresh)
    else:
     cache[n] = S(f) + G((n-f))
  return cache[n]
print S(cap)
