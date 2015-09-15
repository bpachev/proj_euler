from proj_euler import mark_primes

import numpy as np
import itertools



def lcs_lens(xs, ys):
    lens = np.zeros((len(xs)+1,len(ys)+1),dtype=np.int16)
    dirs = np.zeros((len(xs)+1,len(ys)+1),dtype=np.uint8)
    curr = lens[0,:]
#    print xs,ys
    for j,x in enumerate(xs):
        prev = curr
        curr = lens[j+1,:]
        for i, y in enumerate(ys):
            if x == y:
                curr[i + 1] = prev[i] + 1
                dirs[j+1,i+1] = 3 #diagonal arrow
            else:
                if curr[i] > prev[i + 1]:
                 curr[i+1] = curr[i]
                 dirs[j+1,i+1] = 1 #along x 
                elif prev[i + 1] > curr[i]:
                 curr[i+1] = prev[i+1] 
                 dirs[j+1,i+1] = 2 #along y
                else:
                 curr[i+1] = curr[i]
                 dirs[j+1,i+1] = 4 #both are optimal
#    print lens
    return dirs


def digital_root(a):
 if a < 10:
  return a
 else:
  return digital_root(sum(map(lambda x: int(x),str(a))))
def seq_to_ans(N,mod):
 res = 0
 for n in N:
  res = (10*res+n)%mod
 return res

def best_seq(dirs,p,c):
 res = []
 x,y = len(p),len(c)
# print dirs
 while True:
#  print x,y,dirs[x,y],p[x-1],c[y-1]
  if dirs[x,y] == 2:
    x -= 1
    res.append(p[x])
  elif dirs[x,y] == 1:
    y-=1
    res.append(c[y])
  elif dirs[x,y] == 4:
    if c[y-1] < p[x-1]:
      y-=1
      res.append(c[y])
    elif p[x-1] < c[y-1]:
      x-=1
      res.append(p[x])
    else:
     print "ARGG"
  elif dirs[x,y]==3:
    x-=1
    y-=1
    res.append(c[y])
  else:
    return res
  if not x:
    return res+c[:y][::-1]
  if not y:
    return res+p[:x][::-1]
  
 return res


def solve(l=10):
 p = []
 c  = []
 mod = 10**9+7
 cap = 10**5+10**4
 mask = mark_primes(cap);
 for i in xrange(2,cap):
  if mask[i] and len(p) < l:
    p.append(digital_root(i))
  elif len(c) < l:
    c.append(digital_root(i))
 dirs = lcs_lens(p[::-1],c[::-1])
 seq = best_seq(dirs,p[::-1],c[::-1])
 return seq_to_ans(seq,mod)

print solve(10000)

