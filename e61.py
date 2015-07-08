from itertools import permutations
import sys
PNumArrs = []

def PentArr(f):
 res = {}
 for i in xrange(1000):
   o = f(i)
   if o > 10**4:
     break
   #has 3 digits and third digit non-zero
   if o > 10**3 and (o/10) % 10:
     p1 = o / 100
     p2 = o % 100 
     if not p1 in res:
      res[p1] = [p2]
     else:
      res[p1].append(p2)
 return res


PNumArrs.append(PentArr(lambda i: i*(i+1)/2)) #triangular
PNumArrs.append(PentArr(lambda i: i*i)) #square
PNumArrs.append(PentArr(lambda i: i*(3*i-1)/2)) #pentagonal
PNumArrs.append(PentArr(lambda i: i*(2*i-1))) #hexagonal
PNumArrs.append(PentArr(lambda i: i*(5*i-3)/2)) #Heptagonal
PNumArrs.append(PentArr(lambda i: i*(3*i-2))) #octagonal

def follow_chain(mask,index,chain_len,chain_start,curr):
  global PNumArrs
  if index == chain_len:
    if not curr == chain_start:
      return -10**20 
    else:
      return curr*101
  else:
    if not curr in PNumArrs[mask[index]]:
      return -10**9
    else:
      for next in PNumArrs[mask[index]][curr]:
       r = 101*curr + follow_chain(mask,index+1,chain_len,chain_start,next)
       if r > 0:
         return r
      return r


for mask in permutations(range(5)):
  #iterate over all initial octogonal numbers
  for t in PNumArrs[5]:
    s = follow_chain(mask,0,5,t,PNumArrs[5][t][0])
    if s > 0:
      print t
      print s
      print mask
      
    
    
