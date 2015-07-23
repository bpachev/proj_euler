from bisect import bisect_left,bisect_right
import numpy as np
from proj_euler import HarshadGen


cap = 10**11
pcap = cap
depth = 5 #3**depth solutions to x^3-1 = 0 (mod n)
divs = [7,9,13,19,31]

for i in xrange(depth-1):
  pcap /= divs[i]

mask = np.zeros(pcap+1,dtype=int)

#code 0 = not marked,1 marked, but not by 9, or a prime equal to one mod 6, 2, otherwise

good = [] #9 + primes 1 mod 6
bad = [1] #everything not divisible by 'good' nums
bsums = [1] #partial sums of the previous array

for i in xrange(2,pcap+1):
  if i ==9:
    for j in xrange(i,pcap+1,9):
      mask[j] = 2
    good.append(i)
  if mask[i] == 0:
    if i%3==1:
     good.append(i)
     m = 2
    else:
     bad.append(i)
     bsums.append(bsums[-1]+i)
     m = 1
    for j in xrange(i,pcap+1,i):
     if m > mask[j]:
      mask[j] = m
  elif mask[i] == 1:
    bad.append(i)
    bsums.append(bsums[-1]+i)
print "Num bases %d, num non-bases %d " % (len(good),len(bad))
s = 0
B1 = int(cap**(.2))+1
for i1,p1 in enumerate(good):
 if p1>B1:
  break
 B2 = int((cap/p1)**(1./4))+1
 for i2,p2 in enumerate(good[i1+1:],i1+1):
  if p2 > B2:
   break
  B3 = int((cap/p1/p2)**(1./3))+1
  for i3,p3 in enumerate(good[i2+1:],i2+1):
   if p3 > B3:
    break
   B4 = int((cap/p1/p2/p3)**(1./2))+1
   for i4,p4 in enumerate(good[i3+1:],i3+1):
    if p4 > B4:
     break
    for i5,p5 in enumerate(good[i4+1:],i4+1):
     prod = p1*p2*p3*p4*p5
     if prod > cap:
      break
     for n in HarshadGen((p1,p2,p3,p4,p5),cap):
       pos = bisect_right(bad,cap/n)
       s += n*bsums[pos-1]
print s

#   if p1*p2 <= cap:
#     print p1,p2,bad[:bisect_right(bad,cap/(p1*p2))],bsums[bisect_right(bad,cap/(p1*p2))-1]




