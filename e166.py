from itertools import product

l = range(10)
s = {i:[] for i in xrange(4*9+1)}

for t in product(l,repeat=4):
 s[sum(t)].append(t)

#A = np.zeros((8,8))
#A[0,:4] = np.ones(4)
#A[1,4:] = np.ones(4)
#for i in xrange(4):
# A[i+2,i] = 1
# A[i+2,i+4] = 1
#A[6,1],A[6,4]=1,1
#A[7,2],A[7,7] = 1,1
tot =0

print s[36]
for i in s:
 print i,tot
 for t1,t2 in product(s[i],s[i]):
  s1,s2,d1,d2 = t1[0]+t2[0],t1[3]+t2[3],t1[3]+t2[2],t1[0]+t2[1]
  for c1 in xrange(i-max(d1,s1)+1):
   t31 = i-c1-s1
   t32 = i-c1-d1
   t42 = i-t32-t1[2]-t2[2]
   if t42 < 0:
    continue
   c2 =  (i-d2-s2+t31+t32)
   if c2%2:
    continue
   c2 /= 2
   t43,t34,t33 = i-c1-c2-t42,i-c2-s2,i-c2-d2
   if not t31+t32+t33+t34==i or not c1+t42+t43+c2 == i or not t1[1]+t2[1]+t32+t42 == i or not t1[2]+t2[2]+t33+t43 == i:
    continue
   if c1<0 or c1>9 or t43 < 0 or t43>9 or t42 < 0 or t42>9 or t34 < 0 or t34>9 or t32 < 0 or t32>9 or t31 < 0 or t31>9 or t33 < 0 or t33>9 or c2 < 0 or c2>9:
    continue
   tot += 1
  
    
  
print tot 



