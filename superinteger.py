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

def max_overlap(a,b):
 '''
 The maximum overlap length between a and b, with a first
 '''
 la,lb = len(a),len(b)
 for i,x in enumerate(a):
   j = 0
   while b[j] == a[j+i]:
     j += 1
     if j == l or i+j==la:
       return j


p = []
c  = []
mod = 10**9+7
cap = 10**5+10**4
l = 20

mask = mark_primes(cap);
for i in xrange(2,cap):
 if mask[i] and len(p) < l:
   p.append(digital_root(i))
 elif len(c) < l:
   c.append(digital_root(i))
#print p,c
dirs = lcs_lens(p,c)  
#print dirs

#the next diagonal step(s) encountered
#hopefully this eliminates exponential memory growth
def explore_branch(x,y):
  global dirs
  while True:
   if not x or not y:
    return set()
   if dirs[x,y] == 2:
    x-=1
   elif dirs[x,y] == 1:
    y-=1
   elif dirs[x,y] == 3:
    return set([(x,y),])
   elif dirs[x,y] == 4:
    return explore_branch(x-1,y).union(explore_branch(x,y-1))
   else:
    return set()

def seqs(x,y):
  global dirs,p,c
  if not x or not y:
   return []
  pref = []
  while True:
   if dirs[x,y] == 2:
    x = x-1
   elif dirs[x,y] == 1:
    y = y-1
   elif dirs[x,y] == 3:
    pref.append(p[x-1])
    x-=1
    y-=1
   elif dirs[x,y] == 4:
    #branch
    res = []
 #   print explore_branch(x-1,y).union(explore_branch(x,y-1)),x,y,dirs[x,y]
    for tup in explore_branch(x-1,y).union(explore_branch(x,y-1)):
     p1 = seqs(tup[0],tup[1])
     for sq in p1:
      res.append(pref+sq)
   
    return res
   elif not x or not y:
    return [pref]


def gen_N(seq):
 global p,c
 pit=0
 cit=0
 seq_it = 0
 N = []
 for s in seq:
  while not p[pit] == s or not c[cit] == s:
     if p[pit] == s:
       N.append(c[cit])
       cit+=1
       continue
     if c[cit] == s:
       N.append(p[pit])
       pit += 1
       continue
     if p[pit] < c[cit]:
      N.append(p[pit])
      pit += 1
     else:
      N.append(c[cit])
      cit += 1
  N.append(s)
  pit+=1
  cit+=1

 while not pit == l or not cit == l:
     if pit == l:
       N.append(c[cit])
       cit+=1
       continue
     if cit == l:
       N.append(p[pit])
       pit += 1
       continue
     if p[pit] < c[cit]:
      N.append(p[pit])
      pit += 1
     else:
      N.append(c[cit])
      cit += 1
 return N

def seq_to_ans(N,mod):
 res = 0
 for n in N:
  res = (10*res+n)%mod
 return res

def seqs_new(x,y):
 global dirs,p
 pref = []
 

print "generated dirs"
seq = seqs(l,l)
cands = [gen_N(s[::-1]) for s in seq]
#print seq,dirs
#print p,c
print len(set(tuple(c) for c in cands))
print "Total %d cands" % len(cands)
print min(cands)
print seq_to_ans(min(cands),mod)
