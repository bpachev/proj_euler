import numpy as np
T = [i*(i+1)/2 for i in xrange(1000)]
cap = 2*10**4
init = lambda w,h,l : 2*(w*h+h*l+l*w)
mask = np.zeros(cap,dtype=int)
def layer(w,h,l,n):
  global T
  if n==1:
    return init(w,h,l)
  else:
    return init(w,h,l) + 4*(n-1)*(w+h+l) + 8*T[n-2]

for w in xrange(1,cap/4):
  for h in xrange(1,min(w,cap/w)+1):
    for l in xrange(1,min(h,cap-2*w*h)+1):
      i,t = 1,init(w,h,l)
      if t > cap:
        break
      while t < cap:
        mask[t] += 1
        i += 1
        t = layer(w,h,l,i)

K = 1000
for i in xrange(cap):
  if mask[i] == K:
    print i
    break
 
