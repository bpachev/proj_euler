import numpy as np

def pow_double_sum(mod,k,N):
  '''
  Assumes mod is prime.
  sum of sum of kth powers from 1 to n
  '''
  bernoulli = np.zeros(k+2,dtype=np.int64)
  pow_sums = np.zeros(k+2,dtype=np.int64)
  binoms = np.zeros(k+2,dtype=np.int64)
  
  for i in xrange(k):
  
