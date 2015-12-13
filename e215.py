def count_walls(n):
 l=[0,1,1]
 for i in xrange(n-2):
  l.append(l[-2]+l[-3])
 print l

def gen_walls(n):
 l=[[[2]],[[3]],[[2,2]]]+[[] for i in xrange(n-4)]
 for i in xrange(n-4):
  for el in l[i]:
   l[3+i].append(el+[3])
  for el in l[i+1]:
   l[3+i].append(el+[2])
 return l

def is_compatible(w1,w2):
 c1=0
 c2=w2[0]
 i2=1
 l2=len(w2)
 for el in w1:
  c1 += el
  while c2 < c1:
   c2+=w2[i2]
   i2+=1
  if c2==c1:
   if i2==l2:
    return True
   else:
    return False
 return True


def solve(n,k):
 walls = gen_walls(n)[-1]
 l=len(walls)
 state = [1 for i in xrange(l)]
 tdict = {i:[] for i in xrange(l)}
 for i,w1 in enumerate(walls):
  for j,w2 in enumerate(walls):
   if is_compatible(w1,w2):
    tdict[i].append(j)
 
 for i in xrange(k-1):
  temp = [0]*l
  for j in tdict:
   for k in tdict[j]:
    temp[k]+=state[j]
  state=temp
  
 return sum(state)
print solve(32,10)
 
