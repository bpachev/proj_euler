
#def isqrt(n):
    #x = n
    #y = (x + 1) // 2
    #while y < x:
        #x = y
        #y = (x + n // x) // 2
    #return x
  
  
aprev = 1
bprev = 2
acurr = 0
bcurr = 0

for i in xrange(20):
  acurr = 2*bprev + aprev
  bcurr = 2*acurr + bprev
  aprev = acurr
  bprev = bcurr
  if acurr > 10**12: 
    print str((acurr+1)/2)
    break