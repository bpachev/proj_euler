sc = {} #summatory cache
oc = {} #odd summatory function
fc = {} #summand cache

cap = 100
mod = 10**9

def S(n):
 global sc
 if n in sc:
   return sc[n]
 if not n:
   return 0
 if n == 1:
   return 1
 if n == 2:
   return 2
   return 6
 sc[n] = (S(n/2) + O(n)) % mod
 return sc[n] 


def O(n):
 global oc
 if n in oc:
   return oc[n]
 if not n:
   return 0
 if n == 1:
   return 1
 if n == 2:
   return 1
 if n == 3 or n == 4:
   return 4
 r = n % 4
 if r == 3:
  oc[n] = (5*O(n/2) - 3 * S(n/4)) % mod
 elif r == 1:
  oc[n] = (5*O((n+1)/2) - 3 * S(n/4) - F(n+2)) % mod
 elif r == 2:
  oc[n] = (5*O(n/2) - 3 * S(n/4) - F(n+1)) % mod
 else:
  oc[n] = (5*O((n-1)/2) - 3 * S((n-1)/4)) % mod
 oc[n] -= 1
 return oc[n]

def F(n):
 global fc
 if n in fc:
  return fc[n]  
 
 if n == 1 or n == 3 or n == 0:
  return n
 
 t = n
 r = n%4
 if r==1:
  fc[n] = (2*F(2*(n/4) + 1) - F(n/4) ) % mod
 elif r==3:
  fc[n] = (3*F(2*(n/4) + 1) - 2*F(n/4)) % mod
 else:  
  while t %2 == 0:
   t /= 2
   fc[n] = F(t)
 return fc[n]

print S(3**37)

