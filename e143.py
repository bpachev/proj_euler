from itertools import combinations
cap = 120000
l = [i**2 for i in xrange(2*cap)]
sqs = set(l)
pairs = {i:set() for i in xrange(2*cap)} #p and q s.t. p*p+p*q+q*q is a square

reps = [[] for i in xrange(2*cap)]

#The theoretical basis for this code is the representation of naturals as x^2+3*y^2
#Numbers of this form are closed under mutliplication.


#looks at a candidate j and q with j*j + 3*q*q a square and gets p and q qith p*p+p*q+q*q a square.
def consider(j,q):
 global pairs
 p = (j-q)/2
 if (j-q)%2 == 0 and p > 0 and p < cap and q > 0:
   pairs[p].add(q)
   pairs[q].add(p)

for i in xrange(1,int((2*cap)**.5)+1):
 for j in xrange(1, int(((2*cap-i*i)/3.)**.5)+1):
  reps[l[i] + 3*l[j]].append((i,j)) 

for i in xrange(1,2*cap):
 if len(reps[i]) and reps[i][0] is not None:
  #find reps for i*i
  treps = []
  for n,rep1 in enumerate(reps[i]):
   for rep2 in reps[i][n:]:
    a,b = rep1
    c,d = rep2
    treps.append((abs(a*c-3*d*b),a*d+b*c))
    treps.append((a*c+3*d*b,abs(a*d-c*b)))

  for j,q in treps:
   consider(j,q)
   consider(j+3*q,abs(j-q)) #handle mult by 4
   consider(abs(j-3*q),j+q)
  

  #search for things higher than it that need reps
  for j in xrange(i,2*cap,i):
   if not len(reps[j]):
    mul = j/i
    for a,b in treps:
     a,b, = a*mul,b*mul
     consider(a,b)
     if j%2:    
      consider(a+3*b,abs(a-b))
      consider(abs(a-3*b),a+b)

def old(cap):
 l = [i**2 for i in xrange(2*cap)]
 sqs = set(l)
 pairs = {i:set() for i in xrange(2*cap)} #p and q s.t. p*p+p*q+q*q is a square
 nfound=0
 for p in xrange(1,cap):
  for q in xrange(p+1,cap-p):
   if l[p]+l[q]+p*q in l:
    pairs[p].add(q)
    print p,q,(p*p+p*q+q*q)**.5
    nfound+=1
 print nfound
res = set()
for p in pairs:
 for q,r in combinations(pairs[p],2):
  if q in pairs[r]:
   if p+q+r <= cap:
    res.add(p+q+r)
print sum(res)  
