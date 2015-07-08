import proj_euler as pe

mod = 10**9

def base_dec(l,b):
  for i in xrange(len(l)):
    if l[i]:
      l[i] -= 1
      for j in xrange(i):
       l[j] = b-1
      return


def fast_forward(d,k):
  global mod
  '''
  GIVEN d, a list representing a number in base k (reversed, d[0] = NUM%k)
  fast track d to have the last two digits zero, updating d and k appropriately
  RETURNS: the new k
  '''
  if not d[0]:
    base_dec(d,k+1)
    k += 1
  if len(d) == 1 or not d[1]:
    #Trivial case
    ret = d[0]
    d[0] = 0
    return ret + k
  
  else:
    ret = d[0] + (pow(2,d[1],mod)-1) * (d[0] + k + 1)
    d[0] = 0
    d[1] = 0
    return ret + k

def F_new(g):
  k = 2
  d = pe.base_repr(g,2)
  
  while True:
    k = fast_forward(d,k) % mod
    if not sum(d):
      return (k-2) % mod
    else:
     k += 1    
     base_dec(d,k)
  

print sum([F_new(i) for i in xrange(1,16)]) % mod
