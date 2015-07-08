import proj_euler as pe
import numpy as np
mod = 1000000123

#no leading zeros
def f(n,pMask):
  global mod
  s = 0
  if not n:
    return 0
  if n == 1:
    for i in pMask:
      if i == 1:
        s += 1
    return s
  for i in xrange(0,2**10):
    t = i
    r = []
    l = []
    j = 0
    while t:
     if pMask[j]:
        if t&1:
          r.append(0)
          l.append(1)
        else:
          r.append(0)
          l.append(1)          
     else:
        if t&1:
          r.append(1)
          l.append(1)
        else:
          r.append(0)
          l.append(0)          
      
     j += 1
     t/=2
    s = (s + f(n/2,r) * f(n-n/2,l)) % mod
  return s

#All that matters is the NUMBER of evens/odds in a certain state, not which ones
T = np.zeros((21**2,21**2)).astype(np.int64)
#(num evens parity 0, 1, not present, num odds parity 0, 1, not present), maps to the row
state_dict = {}
#reverse lookup
rev_dict = {}
sList = []
for i in xrange(6):
  for j in xrange(6 - i):
    k = 5 - j-i
    sList.append([i,j,k])

c = 0
for t1 in sList:
  for t2 in sList:
     state_dict[tuple(t1+t2)] = c
     rev_dict[c] = tuple(t1+t2)
     c += 1

def mark_transitions(state,state_num,s1,s2):
  global T, state_dict
  if not state[s1]:
    return
  else:
    new_state = [state[i] for i in xrange(6)]
    num_transitions = new_state[s1]
    new_state[s1] -= 1
    new_state[s2] += 1
    new_state_num = state_dict[tuple(new_state)]
   # print str(num_transitions)+ " trans from " + str(state) + " to " + str(new_state)
    #print str(state_num) + " " + str(new_state_num)
    T[new_state_num,state_num] += num_transitions
    

for state1 in xrange(c):
  st = list(rev_dict[state1])
  mark_transitions(st,state1,2,1)
  mark_transitions(st,state1,1,0)
  mark_transitions(st,state1,0,1)
  mark_transitions(st,state1,5,4)
  mark_transitions(st,state1,4,3)
  mark_transitions(st,state1,3,4)
  T[state1,]
      
def test_transitions(t1,t2):
  global T,state_dict
  print T[state_dict[t2],state_dict[t1]]


#test_transitions((5,0,0,5,0,0),(4,1,0,5,0,0))

init = np.zeros(21*21).astype(np.int64)
init[state_dict[(0,0,5,0,1,4)]] = 5 #five different starting odd numbers
init[state_dict[(0,1,4,0,0,5)]] = 4 #cannot start with zero
s = 0
def good_vals(res):
  s = 0
  for state in state_dict:
    if not state[1] and not state[3]:
      s += res[state_dict[state]]
  return s

#assumes n = 2^n-1
def matrix_sum_mod(n,T,I,mod,safe=True):
  s = 0 #don't include Q(1)
  SumAccum = I
  Accum = T
  while n:
    if not safe:
      SumAccum = np.remainder(np.dot(Accum,SumAccum),mod) + SumAccum
      Accum = np.remainder(np.dot(Accum,Accum),mod)
    else:
      SumAccum = pe.safe_matrix_vector_dot(Accum,SumAccum,mod) + SumAccum
      Accum = pe.safe_matrix_mul(Accum,Accum,mod)
    s = (s + good_vals(SumAccum)) % mod    
    n/= 2 
  print s   
  return SumAccum

print good_vals(matrix_sum_mod(2**39-1,T,init,mod,True))  


#s = good_vals(init)
#for i in xrange(1,8):
 # s += good_vals(pe.matrix_mod_exp(i,T,init,mod))
#print s

