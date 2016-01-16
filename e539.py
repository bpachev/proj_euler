def p(N,side=0):
 if N <= 1:
  return N
 if not side:
  return 2*p(N/2,1)
 else:
  if not N%2:
   return 2*p(N/2,0)-1
  else:
   return 2*p(N/2,0) 

def dec(i,N):
 s=0
 for j in xrange(1,N+1):
  if j>=2**(i+1) and not j&(2**i):
   s+=1
 return s 
def ndec(i,N):
 p2=2**i
 res=p2*(N/(2**(i+1)))
 if not (N&2**i):
  res += N%p2-p2+1
 return res
 
def s(N):
 i=0
 res=0
 while 2**i <= N:
  if i%2:
   res -= 2**i*ndec(i,N)
  i +=1
 res +=(4**(i)-1)/3 
 res -= (2**i-N-1)*2**(i-1)
 return res

print s(10**18),s(10**18)%987654321 
print sum([p(i) for i in xrange(1,1001)])
