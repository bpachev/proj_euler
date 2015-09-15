
from proj_euler import argsort,init_fact
from itertools import permutations

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
def permu_order(l,fact):
  t = argsort(argsort(l))
  if len(t) <= 1:
    return 1
  else:
   return fact[len(t)-1] * t[0] + permu_order(l[1:],fact)
facts = init_fact(21)
pref = [2,1,3,4,6,8,10,12]
i = 0
m = 10**100
for p in permutations([15, 17, 16, 19, 18, 14, 11, 9, 7,  5 ,13,21]):
  i += 1
  if first_sort(pref + list(p)+[20]) == 3**12:
    t = permu_order(pref + list(p)+[20],facts)
    if t < m:
     print t
     m = t
     print pref + list(p)+[20]
 
  if i % 10**6 == 0:
    print "On %d" % i
print m 
