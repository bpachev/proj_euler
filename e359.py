import proj_euler as pe

#Project Euler problem 359, "Hilbert's New Hotel"

s = 0
mod = 10**8

#f = floor, r = room
def P(f,r):
 if f == 1:
   return r*(r+1) / 2
 k = (r-1)/2
 b = [(f*f) / 2]
 nextSquare = 2*(f/2)+1
 b.append((nextSquare)**2 - b[0])
 b.append((nextSquare+1)**2 - b[1]) 
 
 if r <= 3:
   return b[r-1]
 
 else:
   if not r%2:
     a = b[2] - b[0] + 2
     return b[1] +  pe.arithmetic(a,4,k)
   else:
     a = b[2] - b[0]
     return b[0] + pe.arithmetic(a,4,k)

n = 71328803586048
factors = [(2,27), (3,12)]
s = 0
for f in pe.divisors(factors):
  s = (s + P(f,n/f)) % mod

print s
  

