import numpy as np


cap = 1000

#License plates
def f(numSeen,seenMid):
  global cap
  if 2*numSeen +2 > cap:
    return 0
  if seenMid == 2:
    return 0
  
  return cap/(cap-1.-numSeen) * (1 + 1./cap * f(numSeen,seenMid+1) + (cap-2.*numSeen-2) / cap * f(numSeen+1,seenMid))

print f(0,0)
  
