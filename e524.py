from proj_euler import argsort,init_fact
from itertools import permutations

def permu_order(l,fact):
  t = argsort(argsort(l))
  if len(t) <= 1:
    return 1
  else:
   return fact[len(t)-1] * t[0] + permu_order(l[1:],fact)
  
def test_permu_order(k):
 fact = [1]
 for i in xrange(1,k+1):
    fact.append(i*fact[-1])
 i = 1
 for p in permutations(range(1,k+1)):
   if not permu_order(list(p),fact) == i:
    print "ERROR ON " + str(p)
   i += 1

def dumb_solve(n,k):
 fact = [1]
 for i in xrange(1,k+1):
    fact.append(i*fact[-1])
 i=1
 for p in permutations(range(1,n+1)):
  if first_sort(p) == k:
    print p    
    return i
  i += 1

# number of steps in first sort  
def first_sort(p):
 res = 0
 for i,elem in enumerate(p):
  num_greater = 0
  for e2 in p[:i]:
   if e2 > elem:
    num_greater+=1
  if num_greater:
   res += 2 **(i-num_greater)
 return res

def bounding_permu(n):
  b = bin(n)[2:]
  print b
  l = [x for x in range(1,len(b)+2)]
  nl = []
  for bit in b:
    if bit == '1':
     nl.insert(0,l[-2])
     l.remove(l[-2])  
    elif bit == '0':
     nl.insert(0,l[-1])
     l.remove(l[-1])
  return l+nl

def solve(n):
  b = bin(n)[2:]
  fact = init_fact(len(b)+2)
  p = bounding_permu(n)
  if not first_sort(p) == n:
   print "ARRGH"
  print p  
  return permu_order(p,fact)

def new_solve(n):
  b = bin(n)[2:]
  bdigits = len(b)
  print b  
  fact = init_fact(bdigits+2)
  nzeros=0
  pow2 = []
  for i,bit in enumerate(b):
   if bit=='1':
     pow2.append(bdigits-1-i)
   else:
     nzeros += 1
  bound = bounding_permu(n)
  rem = range(1,len(bound)+1)  
  backwards([],rem,list(b))

mx = 10**100
facts = init_fact(46)
  
def find_best(n,bound,curr,rem,nzeros,b):
  global mx,facts
#  print bound,curr,rem,b,nzeros
  c = len(curr)
  if c == len(bound):
   if first_sort(curr) == n:
     t = permu_order(curr,facts) 
     if  t < mx:
       mx = t
       print "New min %d" % t
     return 
  if curr == bound[:c]:
   for i,r in enumerate(rem):
    if r > bound[c]:
     break
    if not r:
     continue
    t = r
    #get the contribution of the proposed addition
    s = 0
    for e in curr:
     if e > r:
      s += 1
 #   print r,s 
    if not s:
     if nzeros:
      rem[i] = 0
      find_best(n,bound,curr+[t],rem,nzeros-1,b)   
      rem[i] = t   
     else:
      continue
    else:
#     print -1+s-c
     if b[-1 + s-c] == '1':
      b[-1 + s-c] = '0'
      rem[i] = 0
      find_best(n,bound,curr+[t],rem,nzeros,b)   
      rem[i] = t        
      b[-1 + s-c] = '1'
     else:
      continue 
   return
    
  
  for i,r in enumerate(rem):
   if not r:
    continue
   t = r
   #get the contribution of the proposed addition
   s = 0
   for e in curr:
    if e > r:
     s += 1
   if not s:
    if nzeros:
     rem[i] = 0
     find_best(n,bound,curr+[t],rem,nzeros-1,b)   
     rem[i] = t   
    else:
     continue
   else:
    if b[-1 + s-c] == '1':
     b[-1 + s-c] = '0'
     rem[i] = 0
     find_best(n,bound,curr+[t],rem,nzeros,b)   
     rem[i] = t        
     b[-1 + s-c] = '1'
    else:
     continue 
   
   
  return
    
def backwards(curr,rem,b):
 global mx,facts
# print curr,rem,b
 if not len(rem):
  if first_sort(curr) == n
  t = permu_order(curr,facts)
  if t < mx:
    mx = t
    print first_sort(curr)
    print "New min % d" % t
  return
 c = len(curr)
 if c < len(b) and b[c] == '1':
   #take it or I won't get the chance later on
   b[c] = '0'
   t = rem[-2]
   rem.remove(t)
   backwards([t]+curr,rem,b)
   rem.insert(-1,t)
   b[c] = '1'
   return
 saw_bit = 0
 for i,bit in enumerate(b):
   if bit == '1':
    saw_bit = 1
    b[i] = '0'
    t = rem[len(b)-i-1]
    rem.remove(t)
    backwards([t]+curr,rem,b)
    rem.insert(len(b)-i-1,t)
    b[i] = '1'
 
 if not saw_bit:
   backwards(rem+curr,[],b)
 else:
   t = rem[-1]
   rem.remove(t)
   backwards([t]+curr,rem,b)    
   rem.append(t)
  
    
print dumb_solve(6,23)
new_solve(3**12)
