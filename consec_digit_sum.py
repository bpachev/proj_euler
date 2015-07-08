nSteps = 20
cache = {}

def f(steps,d1,d2):
  if steps == 0:
    return 1
  if (steps,d1,d2) in cache:
    return cache[(steps,d1,d2)]
  
  s = 0
  for i in xrange(0,10-d1-d2):
    s += f(steps-1,d2,i)
  cache[(steps,d1,d2)] = s
  return s

nDigits = 20
s = 0
for i in xrange(1,10):
  s += f(nDigits-1,0,i)
print s
  
