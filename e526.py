from proj_euler import MillerRabin, shanks_factorize

def f(n):
  f = shanks_factorize(n)
  return max(f.keys())

def g(n):
  return sum([f(n+i) for i in xrange(9)])
  
N = 10**16
mx = 0

#WE must have i 3 mod 7, 1,2 mod 4, and 1 mod 3
# SO i == 10 or 73 mod 84
#If i is 10 mod 84, then 2|30*i+14 and 4|30i+16
#We then require that (30i+14)/2 is prime and (30i+16)/4 is prime, and (30i+18)/6 is prime
#If i == 73 mod 84, we require that (30i+14)/4 is prime and (30i+16)/2 is prime, and (30i+12)/6 is prime  
M = 4*7
for j in xrange(1,M):
 if (j%4==1 or j%4 == 2) and j%7 ==3: 
   print j

i = (N/30)
#j = i/M
j = 11904741107142
nsols = 0
while j>0:
 i1 = 30*(M*j+10)
 if MillerRabin(i1+11) and MillerRabin(i1+13) and MillerRabin(i1+17) and MillerRabin(i1+19):
   if MillerRabin((i1+14)/2) and MillerRabin((i1+16)/4) and MillerRabin((i1+18)/6):
#     t = g(i1+11)
     t  = (i1+11)+(i1+13)+(i1+17)+(i1+19) + (i1+14)/2 + (i1+16)/4 + (i1+18)/6 + f(i1+12)+f(i1+15)
     nsols+=1
     print i1
     if t > mx:
      print "New max %d on %d" % (t, i1)
      mx = t

 
 
 i2 = 30*(M*j+17)
 if MillerRabin(i2+11) and MillerRabin(i2+13) and MillerRabin(i2+17) and MillerRabin(i2+19):
   if MillerRabin((i2+14)/4) and MillerRabin((i2+16)/2) and MillerRabin((i2+12)/6): 
#     t = g(i2+11)
     nsols += 1
     print i2
     t  = (i2+11)+(i2+13)+(i2+17)+(i2+19) + (i2+14)/4 + (i2+16)/2 + (i2+12)/6 + f(i2+18)+f(i2+15)
     if t > mx:
       print "New max %d on %d" % (t, i2)
       mx = t
 if not j % 10**5:
     print "ON j = %d, found %d sols so far" % (j,nsols)
 j -= 1
 
print "max %d" % mx  
