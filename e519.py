import numpy as np
import sys

sys.setrecursionlimit(10**6)

mod = 10**9
cap = 20000

cache = {}

def fountains(n,lastDiag):
  global mod
  if not n:
    return 1
  if n in cache:
    if lastDiag in cache[n]:
      return cache[n][lastDiag]
  else:
    cache[n] = {}
  diagLen = max(lastDiag-1,1)
  s = 0
  while diagLen*(diagLen+1)/2. <= n:
    if lastDiag == 0:
      if diagLen == 1:
        s = (s + 3*fountains(n-diagLen, diagLen)) % mod
      else:
        s = (s + 6*fountains(n-diagLen, diagLen)) % mod
    elif lastDiag == 1:
      if diagLen == 1:
        s = (s + 2*fountains(n-diagLen, diagLen)) % mod
      else:
        s = (s + 4*fountains(n-diagLen, diagLen)) % mod
    else:
       s = (s + fountains(n-diagLen, diagLen)) % mod
    
    diagLen += 1      
    
  cache[n][lastDiag] = s
  return s
    
print fountains(cap,0)
