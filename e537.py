from proj_euler import primes_and_mask
import numpy as np

k = 20000
mod=1004535809
primes = np.array(primes_and_mask(5*10**5)[0][:k+1])
A1 = np.zeros(k+1,dtype=np.int64)
A1[1:] = primes[1:]-primes[:-1]
A1[0] = 1

def seq_mult(a,b,mod):
 '''
 Given two polynomials of degree at most n with coefficients given by a and b, numpy arrays.
 This function returns the first n coefficients of a*b, modulo mod.
 '''
 n=a.size
 if not n == b.size:
  raise ValueError("Input arrays must have the same shape in seq_mult.")
 res = np.zeros(n,dtype=np.int64)
 for i in xrange(n):
  res[i:] = np.remainder(res[i:] + b[i]*a[:n-i],mod)
 return res

t=k
accum = np.zeros(k+1,dtype=np.int64)
accum[0] = 1
temp = np.copy(A1)
#print temp, accum
while t:
 if t&1:
  accum = seq_mult(accum,temp,mod)
 temp = seq_mult(temp,temp,mod)
 t/=2
print accum[-1]
 
