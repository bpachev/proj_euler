from math import log
def B(i):
 r=0
 while i:
  r += i&1
  i/=2
 return r

def U(i):
 return 2**B(3*i) + 3**(B(2*i)) + B(i+1)

n=3*10**6
a = map(U,range(1,5))
a.sort()
a=a[::-1]
def add(i):
 global a
 
 if i < a[-1]:
  return False,None
 for j,el in enumerate(a):
  if i>el:
   a.insert(j,i)
   break
 for j in xrange(0,len(a)-4):
  if a[j] < sum(a[j+1:j+4]):
   a = a[:j+4]
   return sum(a[j:j+4]),j 
 return False,None

def obj(l):
 P = sum(l)
 if len(l)<4:
  return 0
 return (P-2*l[0])*(P-2*l[1])*(P-2*l[2])*(P-2*l[3])

brack = [[] for i in xrange(int(log(n)/log(2))+3)]
s = sum(a)
tot = s
curr = 1
ind = 0
for i in xrange(1,5):
 brack[B(i)].append(U(i))

for i in xrange(5,n+1):
 u,b = U(i),B(i)
 if b >= curr:
  brack[b].append(u)
  if len(brack[curr+1]) >= 4:
   curr+=1
  brack[curr].sort()

 
 r,ind_new=add(u)
 if r:
  s=r
  ind = ind_new
 o1,o2 = obj(brack[curr][-4:]),obj(a[ind:ind+4])
 if o1 > o2:
  tot += sum(brack[curr][-4:])
 else:
  tot += s
print tot,s,a

#print brack,curr,brack[curr] 
