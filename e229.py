import proj_euler as pe
import numpy as np
cap = 2*10**9
primes,mask = pe.primes_and_mask(int(cap**.5))

def f_old(cap):
  global primes, mask
  sq = set()
  sqList = []
  for i in xrange(1,int(cap**.5)+1):
    sq.add(i*i)
    sqList.append(i*i)

  s1 = set()
  s2 = set()
  s3 = set()
  s7 = set()

  for i in sqList:
    for j in sqList:
      t1 = i+j
      if t1 > cap:
        break
      s1.add(t1)
      t2 = i + 2*j
      t3 = i + 3*j
      t7 = i + 7*j
      if t2 <= cap:
        s2.add(t2)
        if t3 <= cap:
          s3.add(t3)
          if t7 <= cap:
            s7.add(t7)
  q = s1.intersection(s2.intersection(s3.intersection(s7)))
  print len(q)
  return q

FULL_MASK = 15
mods = {1:(4,[1],1), 2:(8,[1,3],2), 3:(3,[1],4), 7:(7,[1,4,2],8)}

def repr_mask(n,res=False):
 global mods
 m = 0
 for i in mods:
   t = mods[i]
   if not res and n < i:
     continue
   if n % t[0] not in t[1]:
     continue
   else:
    m = m | t[2]
 return m 

def spec_is_prime(n):
  global cap,mask
  if n*n <= cap:
   return mask[n]
  else:
   return pe.MillerRabin(n)

def boundedProds(a,n,prod):
  if n <= 1:
    return n
  s = 0
  if prod > 1:
    s = int(np.sqrt(n))
  
  for i in xrange(len(a)):
    if a[i] >n:
      break
    s += boundedProds(a[i+1:],n/a[i],prod*a[i])
  return s

def f(cap):
  global FULL_MASK,primes
  s = 0
  sq = int(cap**.5)
  sq_mask = np.zeros(sq+1).astype(int)
  for p in primes:
    m = repr_mask(p)
    if p == 2:
     m = 4    
    if m:
      for i in xrange(p,sq+1,p):
        sq_mask[i] |= m
  for i in xrange(4,sq+1,4):
    sq_mask[i] |= 12 
  #Get all squares that admit all four representations
  foo = []
  for i in xrange(sq+1):
    if sq_mask[i] == FULL_MASK:
      s += 1
#      print i
#      foo.append(i)
#  print sq_mask[3]
  #now generate all primes
  print "curr_s = " + str(s) 
  good_rems = []
  p = 168 #3*8*7
  for r in xrange(1,p):
    if repr_mask(r,True) == FULL_MASK:
       good_rems.append(r)
  
  good_p = []
  for k in xrange(0,cap/p+1):
    for r in good_rems:
      t = k*p+r
      if spec_is_prime(t):
        if len(good_p) and cap/t  < good_p[0]:
          s += int((cap/t)**.5)
        else:
          good_p.append(t)
  print "found " + str(len(good_p)) + " good primes"
  return s + boundedProds(good_p,cap,1)

#f(cap)
#f_old(cap)
#print len(f(cap))
print f(cap)
#q2= f_old(cap)
#for q in q2:
 # if q**.5==int(q**.5):
  #  if int(q**.5) not in q1:
   #   print str(q) + " foo" 
   # print q**.5
#for p in q:
 # if p*p not in q2:
  #  print str(p) + " hi"
