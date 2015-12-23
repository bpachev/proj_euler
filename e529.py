from proj_euler import *
import numpy as np
import sys
def bounded_digit_sums(n=10,maxd=10):
 '''
 returns all tuples of digits >=1, <=maxd with sum less than n
 '''
 res = [[]]
 last_res,tres = [[]],[]
 for num_ds in xrange(1,n+1):
  for el in last_res:
   s = sum(el)
   for d in xrange(1,maxd):
    if s+d>=n:
     break
    else:
     tres.append(el+[d])
  res.extend(tres)
  last_res = tres
  tres = []
 print sum([len(el)+1 for el in res])
 return res

def new_state(s,d):
 """
 Given we are in state s (all the most recent nonzero digits with sum < 10),
  and we know where the last 10-substring ended with respect to those digits
  this function determines the new state given that digit d is appended.
 If appending d would make it impossible to ever become a 10-substring friendly string 
 (all characters belong to at least 1 substring summing to 10) then None is returned.
 """
 if d==0:
  return s
 t=list(s[0])
 l=len(t)
 for i in xrange(1,l+1):
  ts = d + sum(t[l-i:])
  if ts > 10:
   #i-1 digits from the old state will make it, plus 1 for the added d, so i total elements
   #if we reached this point in the code, no new 10-subtring is being created, thus s[1] will be incremented by 1
   #this is because s[1] is how long ago the last 10-subtring ended
   #if s[1]+1 > i, we can't ever cover everything with a 10-subtring. Fail.
   if s[1]+1 > i:
    return None
   return (tuple(t[l-i+1:]+[d]),s[1]+1)
  elif ts == 10:
   if s[1]>i:
    return None
   return (tuple(t[l-i+1:]+[d]),0)
 
 #If we made it to this line, the sum of all digits in our memory and d doesn't exceed 10, so
 return (tuple(t+[d]),s[1]+1)



def make_transition_matrix():
 basic_states = bounded_digit_sums()
 states = []
 for s in basic_states:
  for l in xrange(len(s)+1):
   states.append((tuple(s),l))
 
 trans_dict = {s:[] for s in states}
 
 for s in states:
  for d in xrange(10):
   ns = new_state(s,d)
   if ns is not None:
    trans_dict[s].append(ns)
#  print s,trans_dict[s]
 term_states=[]
 for s in states:
  if len(s[0]) and not s[1]:
   term_states.append(s)
 T,rd = dict_to_transition_matrix(trans_dict,states,rev_dict=True)
 print T.shape,
 term_inds = [rd[s] for s in term_states]
 return T,states,term_inds

def solve(n,mod=10**9+7):
 T,states,term_inds = make_transition_matrix()
 init=np.zeros(len(states),dtype=np.int64)
 init[0]=1
 res = init
 for i in xrange(n):
  res= T.dot(res)
 s=0
 for i in term_inds:
  s += res[i]
 if len(sys.argv) > 1:
  np.savetxt(sys.argv[1],T,fmt="%d")
 return s%mod
  

