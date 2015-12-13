def b(i):
 r=0
 while i:
  r += i&1
  i/=2
 return r

def U(i):
 return 2**b(3*i) + 3**(b(2*i)) + b(i+1)

n=150
a = map(U,range(1,5))
a.sort()
a=a[::-1]
def add(i):
 global a
 
 if i < a[-1]:
  return False
 for j,el in enumerate(a):
  if i>el:
   a.insert(j,i)
   break
 for j in xrange(0,len(a)-4):
  if a[j] < sum(a[j+1:j+4]):
   a = a[:j+4]
   return sum(a[j:j+4]) 
 return False

s = sum(a)
tot = s
for i in xrange(5,n+1):
 r=add(U(i))
 if r:
  s=r
 tot+=s
print tot,s,a
print map(U,range(1,n)) 
