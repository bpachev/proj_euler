from  proj_euler import primes_and_mask


cap = 10**9
t = 100
primes = primes_and_mask(t)[0]
print primes

def nHamming(minInd,maxNum):
  global primes
  if maxNum <= 1:
    return maxNum  
  s = 1
  i = minInd
  for p in primes[minInd:]:
    if p > maxNum:
      return s
    s += nHamming(i,maxNum/p)
    i += 1
  return s

print nHamming(0,cap)
