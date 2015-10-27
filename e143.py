from itertools import combinations
cap = 1000
l = [i**2 for i in xrange(2*cap)]
sqs = set(l)
pairs = {i:[] for i in xrange(2*cap)} #p and q s.t. p*p+p*q+q*q is a square

reps = [[] for i in xrange(2*cap)]

for i in xrange(1,int((2*cap)**.5)+1):
 for j in xrange(1, int(((2*cap-i*i)/3.)**.5)+1):
  reps[l[i] + 3*l[j]].append((i,j)) 
#print reps
for i in xrange(1,2*cap):
 if len(reps[i]) and reps[i][0] is not None:
  #find reps for i*i
  treps = []
  for rep1,rep2 in combinations(reps[i],2):
   a,b = rep1
   c,d = rep2
   treps.append((abs(a*c-3*d*b),a*d+b*c))
   treps.append((a*c+3*d*b,abs(a*d-c*b)))
  tpairs = []
  for j,q in treps:
   p = (j-q)/2
   if (j-q)%2 == 0 and p > 0 and p < cap:
    if p*p+p*q+q*q not in sqs:
     print "Problem with %d,%d" %(p,q)   
    pairs[p].append(q)
    tpairs.append((p,q))
  #search for things higher than it that need reps
  for j in xrange(i,2*cap,i):
   if not len(reps[i]):
    reps[i][0] = None
    mul = j/i
    for p,q in tpairs:
      pairs[p*mul].append(q*mul)


#nfound=0
#for p in xrange(1,cap):
 #for q in xrange(p+1,cap-p):
  #if l[p]+l[q]+p*q in l:
   #if p not in pairs:
    #pairs[p] = []
   #pairs[p].append(q)
   #nfound+=1
#print nfound

for p in pairs:
 for q,r in combinations(pairs[p],2):
  if l[r]+l[q]+r*q in l:
   print p,q,r,p+q+r
