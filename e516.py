from proj_euler import MillerRabin

def HammingSum(n):
 s = 0
 a2 = 1
 while a2 <= n:
  a3 = a2
  while a3 <= n:
    a5 = a3
    while a5 <= n:
      s += a5
      a5 *= 5
    a3 *= 3
  a2 *= 2
 return s


HammingPrimes = []
nprimes = 0
cap = 10**12
#cap = 1000000
#cap = 100
a2 = 1
while a2 <= cap:
 a3 = a2
 while a3 <= cap:
   a5 = a3
   while a5 <= cap:
     if MillerRabin(a5+1) and a5 < cap and a5 > 5: 
       nprimes += 1
       HammingPrimes.append(a5 + 1)
     a5 *= 5
   a3 *= 3

 a2 *= 2
     
HammingPrimes.sort()

#print HammingPrimes

def sum_hamming_totients(cap,i):
 global HammingPrimes
 global nprimes
 s = HammingSum(cap)
 if cap == 1:
   return 1 
 if not cap:
   return 0
 if i >= nprimes:
   return s
 
 for j in xrange(i, nprimes):
   if HammingPrimes[j] > cap:
     return s
   s += HammingPrimes[j]*sum_hamming_totients(cap/HammingPrimes[j],j + 1)
 return s
   
print sum_hamming_totients(cap, 0) % 2**32  
   
 

