from itertools import izip

bound = 10**8
old = [(0,1,True),(1,100,False)]
i=0
s=0
while True:
  next = []
  new = 0
  last = True
  for f,g in izip(old[:-1],old[1:]):
    if not f[2]:
      if last:
        next.append(f)
      last = f[2]
      continue
    last = f[2]
    p,q = f[0]*g[1]+g[0]*f[1],2*f[1]*g[1]
    if q > bound:
      next.append((f[0],f[1],False))
      continue
    else:
     next.append(f)
     next.append((f[0]+g[0],f[1]+g[1],True))
     s += 1
     new += 1
  i+=1
  if new==1 and i>1:
   print i
   s = s-i+bound/2-50
   break
  if not new:
    break
  next.append(old[-1])
  old = next
print s

