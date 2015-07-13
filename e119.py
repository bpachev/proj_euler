from math import log,floor,ceil

def dsum(n,base=10):
  s = 0
  while n:
    n ,r  = divmod(n,base)
    s += r
  return s

nums = []
IND = 30

start = 10
stop = 100
k = 2

while True:
 minExp = 2 if k == 2 else int(ceil(((k-1)*log(10)) / (log(9)+log(k))))
 maxExp = int(floor(k*log(10)/log(2)))+ 1
# print minExp
# print maxExp
# print k
 for e in xrange(max(minExp,2),maxExp):
   st,sp = max(int(start**(1./e)),2), int(stop**(1./e))+1
#   print st,sp,e,k  
   for n in xrange(st,sp):
     t = n**e
     if n == dsum(t):
       print str(t) + " " + str(dsum(t))
       nums.append(t)
 k += 1
 start *= 10
 stop *= 10
 if len(nums) >= IND:
   nums = sorted(nums)
   print nums
   print "Answer %d" % nums[IND-1]
   print nums[9]
   print nums[1]
   break
