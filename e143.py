from itertools import combinations
cap = 1200
l = [i**2 for i in xrange(2*cap)]
sqs = set(l)
pairs = {} #p and q s.t. p*p+p*q+q*q is a square

reps = [[] for i in xrange(2*cap)]

for i in xrange(1,int((2*cap)**.5)):
 for j in xrange(1, int(((2*cap-i*i)/3.)**.5))
  reps[l[i] + 3*l[j]].append((i,j)) 

for i in xrange(1,2*cap):
 if len(reps[i]) and reps[i][0] is not None:
  #find reps for i*i
  treps = []
  for rep1,rep2 in combinations(reps[i],2):
   a,b = rep1
   c,d = rep2
   treps.append((abs(a*c-3*d*b),a*b+c*d))
   treps.append((a*c+3*d*b,abs(a*b-c*d)))
   
  #search for things higher than it that need reps
  for j in xrange(i,2*cap,i):
   if not len(reps[i]);
    

nfound=0
for p in xrange(1,cap):
 for q in xrange(p+1,cap-p):
  if l[p]+l[q]+p*q in l:
   if p not in pairs:
    pairs[p] = []
   pairs[p].append(q)
   nfound+=1
print nfound

for p in pairs:
 for q,r in combinations(pairs[p],2):
  if l[r]+l[q]+r*q in l:
   print p,q,r,p+q+r
