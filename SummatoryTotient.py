import numpy as np
class TotientSum:
 '''
 A class to find sums involving Euler's totient function.
 In particular, sums of the form sum f(i)*tot(i) i=1 to cap,
 with f totally multiplicative are supported.
 Functions are also provided to handle an additional weight
 of the form g(cap/i) in the sum. The expression cap/i takes on O(sqrt(cap)) distinct values, so the weighted sum may be computed from particular cached values of partial sums of the non-weighted sum. The weighted sum may be computed via the definition for i <= sqrt(n). Let F(n) denote the non-weighted sum up to n. Then the appropriate multiplier by G(k), k > sqrt(n), is F(cap/k) - F(cap/(k-1)). These partial sums are cached as part of the computation of F(cap).
 '''
 def __init__(self,cap,f,fSum,g,mod=10**9,totcache=None):
   '''
   fSum(i,j) is equivalent to sum([f(i) for i in xrange(i,j)])
   It had better not be linear time though.
   g(n) = sum i=1 to n of i*f(i)
   Should also be constant time.
   '''
   self.maxK = int(cap**.5)
   self.kCache = np.zeros(self.maxK+1,dtype=np.int64) #partial sum up to cap/k
   self.mod = mod
   self.cap = cap
   self.g = g
   self.fSum = fSum
   self.f = f
   if not totcache is None:
     self.cache_size = totcache.shape[0]
     self.sCache = np.zeros(cache_size,dtype=np.int64)
     self.sCache[1] = f(1)
     
     for i in xrange(2,self.cache_size):
      self.sCache[i] = (totcache[i]*f(i) + self.sCache[i-1]) % self.mod
     
   else:
     self.cache_size = int(cap**(2./3))+1
     totSum = np.arange(self.cache_size,dtype=np.int64)
     totSum[1] = f(1)
     for i in xrange(2,self.cache_size):
      if totSum[i] == i:
        for j in xrange(i,self.cache_size,i):
          totSum[j] = totSum[j] - totSum[j]/i
      totSum[i] = ((f(i)%mod)*totSum[i] + totSum[i-1]) % self.mod
     self.sCache = totSum
 
 def Sum(self,n,k=1):
   if n < self.cache_size:
     return self.sCache[n]
   if k < self.maxK and self.kCache[k]:
     return self.kCache[k]
   
   s = self.g(n,self.mod)
   
   q,div = n/2,2
   while q >= 1:
    r = n % div
    div_next = div + r/q + 1
    s = (s - self.fSum(div,div_next,self.mod) * self.Sum(n/div,k*div) ) % self.mod
    div = div_next
    q = n/div_next
   if k < self.maxK:
    self.kCache[k] = s
   return s

 def weighted_sum(self,w,start=2):
  '''
  The base case i = 1 is sometimes tricky, so we allow for it to be handled outside of the class.
  '''
  
  s = 0
  for i in xrange(start,self.maxK+1):
    s = ( s + (w(self.cap/i)%self.mod) * (self.Sum(i)-self.Sum(i-1))) % self.mod
    print s,i
  
  for k in xrange(1,self.maxK):
    s = (s + (w(k)%self.mod) * (self.Sum(self.cap/k,k) - self.Sum(self.cap/(k+1),k+1))) % self.mod
  return s
   
  
  
 
 
   
