import numpy as np
import proj_euler as pe
import math

def lattice2d(a,b,sigma = 1):
  '''
  INPUTS: a and b, two numpy arrays with integer entries, both of the same length.
  RETURN the magnitude of the integer linear combination of a and b with shortest length.
  '''
  while True:
    b_mag = np.inner(b,b)
    a_mag = np.inner(a,b)
    mu = a_mag/b_mag
    if abs(mu) >= .5:
      a = a - int(mu)*b
      b_mag = np.inner(b,b)
      a_mag = np.inner(a,b)
      mu = float(a_mag)/b_mag
    a_star = a - mu*b
    
    if np.inner(a_star,a_star) <= (sigma - mu*mu)*b_mag:
      a,b = b,a
    else:
      print b
      print a
      return min(np.sum(np.abs(b)),np.sum(np.abs(a)))

def line_search(a, b):
  #I'm fairly confident the minimum will occur when k makes one of the terms of a - k*b
  # as close to zero as possible, from one side or another.

  n = a.shape[0]
  k_min = 0
  a_min = np.sum(np.abs(a))
  for i in xrange(n):
    #don't divide by zero
    if b[i]:
      temp = np.sum(np.abs(a - (a[i]/b[i])*b))
      if  temp < a_min:
        k_min = a[i]/b[i]
        a_min = temp
     
      
      temp = np.sum(np.abs(a - (a[i]/b[i] + 1)*b))
      if  temp < a_min:
        k_min = a[i]/b[i] + 1
        a_min = temp
  return k_min   
    
def Lagrange_new(a,b):
  #Ensure a has greater norm
  a_norm = np.sum(np.abs(a))
  b_norm = np.sum(np.abs(b))
 # print "Initial a_norm: " + str(a_norm)
  #print "Initial b_norm: " + str(b_norm)

  if a_norm < b_norm: 
    b, a = a, b
    a_norm, b_norm = b_norm, a_norm
  
  a_b = np.sum(np.abs(b - a))
  a_p_b = np.sum(np.abs(b+a))
 # print "Initial |a+b|: " + str(a_p_b)
#  print "initial |a-b|: " + str(a_b)
  if a_b < b_norm:
    b = a - b
#    print "Swapping up the norms"
 #   print "Current |a+b|: " + str(a_p_b)
  #  print "Current |a-b|: " + str(a_b)


  if a_b >= a_norm:
    if a_p_b >= a_norm:
      return b_norm #already reduced
    elif a_p_b < b_norm:
      a = -a #swap a - b and a + b
      b = a - b #do same trick as before
    else:
      a = -a # just swap a-b and a + b

  a_norm = np.sum(np.abs(a)) #just in case something changed

  #while the basis keeps improving
  while a_norm > np.sum(np.abs(b - a)):
    k = line_search(a, b)
    a = a - k*b
    if np.sum(np.abs(a + b)) < np.sum(np.abs(a - b)):
      a = -a
    a, b = b, a
    a_norm = np.sum(np.abs(a))
   # print "a _norm " + str(a_norm) 
  
  #print str() + " " + str(a_norm) + " " + str(np.sum(np.abs(a - b))) + " " + str(np.sum(np.abs(a + b)))
  m = max(np.sum(np.abs(a)), np.sum(np.abs(b)))
  if m > np.sum(np.abs(a - b)) or m > np.sum(np.abs(a + b)):
    print "ERROR. Algorithm not guaranteed to be correct."     
  return min(np.sum(np.abs(a)), np.sum(np.abs(b)))


def Lagrange_shortest_vector(a,b):
  #Ensure a has greater norm
  a_norm = np.sum(np.abs(a))
  b_norm = np.sum(np.abs(b))
  if a_norm < b_norm: 
    b, a = a, b
    a_norm, b_norm = b_norm, a_norm
  
  prev_min = a_norm
  curr_min = b_norm

  #while the basis keeps improving
  while curr_min < prev_min:
    prev_min = curr_min
    k = line_search(a, b)
    a = a - k*b
#    print a
 #   print b
    b, a = a, b
    curr_min = np.sum(np.abs(b))
    
  return min(np.sum(np.abs(a)), np.sum(np.abs(b)))


def tribbo_sum(n,mod = 10**7,past_trib = None):
  s = long(0)
  V = np.zeros(3).astype(np.int64)
  W = np.zeros(3).astype(np.int64)
  curr_trib = np.zeros(12).astype(np.int64)
  if past_trib == None:
    past_trib = np.zeros(12).astype(np.int64)
    past_trib[-1] = 0
    past_trib[-2] = 1
    past_trib[-3] = -1

  for i in xrange(n):
    curr_trib[0] = (past_trib[-1] + past_trib[-2] + past_trib[-3]) % mod
    curr_trib[1] = (curr_trib[0] + past_trib[-1] + past_trib[-2]) % mod
    curr_trib[2] = (curr_trib[1] + curr_trib[0] + past_trib[-1]) % mod
    for j in xrange(3,12):
      curr_trib[j] = (curr_trib[j-1] + curr_trib[j-2] + curr_trib[j-3] ) % mod
    V[0] = curr_trib[0] - curr_trib[1]
    V[1] = curr_trib[2] + curr_trib[3]
    V[2] = curr_trib[4]*curr_trib[5]
    W[0] = curr_trib[6] - curr_trib[7]
    W[1] = curr_trib[8] + curr_trib[9]
    W[2] = curr_trib[10]*curr_trib[11]
   # print V
#    s += min(int(lattice2d(V,W)),np.sum(np.abs(V)), np.sum(np.abs(W)))
#    s += min(np.sum(np.abs(V)), np.sum(np.abs(W)))
    s += Lagrange_new(W, V)
   # print "other version " + str(Lagrange_shortest_vector(W, V))
    curr_trib, past_trib = past_trib, curr_trib
    if (i+1) % 10**5 == 0:
      print str(i/10**5) + " " + str(s)
  return s

I = np.array([[1,0,0],[0,0,1],[0,1,-1]])
T = np.array([[1,1,1],[1,0,0],[0,1,0]])
prev_trib = np.zeros(12).astype(np.int64)
prev_trib[-3:] = pe.recur_mod(2*12*(10**6-10**5),T,I,10**7,True)[0,:]

#print pe.recur_mod(4,T,I,10**7,True)[0,:]

print Lagrange_new(np.array([5,5]),np.array([14,13]))
#print tribbo_sum(10**5,10**7,prev_trib)
