from itertools import combinations as comb
phis = [[1.,0.],[.5,.5]] #rational and irrational parts of phi^n in Q[sqrt(5)]
iphi = [[-.5,.5],[1.5,-.5]] #phi^(-n)
cap = 10**10
ir = 5**.5
phi_to_num = lambda l: l[0] + ir*l[1]
def phi_sum(p1,p2,c1=1,c2=1):
  return [c1*p1[0]+c2*p2[0],c1*p1[1]+c2*p2[1]]
while True:
  if phi_to_num(phis[-1])+phi_to_num(phis[-2]) > cap:
    break
  phis.append(phi_sum(phis[-1],phis[-2]))
  iphi.append(phi_sum(iphi[-1],iphi[-2],c1=-1))

def phi_num(rep):
 global phis
 global iphi
 s = [0.,0.]
 for d in rep:
   s = phi_sum(s,phi_sum(phis[d],iphi[d]))
 return s
 
 

couple_sums = [2]
cInds = [(1,1)]
for i in xrange(2,len(phis)-3):
  if phis[i][1]+phis[i+3][1]+iphi[i][1]+iphi[i+3][1]==0:
   couple_sums.append(int(phis[i][0]+phis[i+3][0]+iphi[i][0]+iphi[i+3][0]))
   cInds.append((i,i+3))
#print couple_sums
sums = set()
s = 0

def compatible(t,i):
  if abs(t[0]-i[0]) ==1 or abs(t[1]-i[0])==1:
    return False
  else:
#   print "Called with " + str(t) + " and " + str(i)
   return True

def pSum(currSum,lastInd):
  global couple_sums,s,cap,cInds
  t = currSum
  if t < cap:
    s += t
#    print t
  else:
    return
  for i in xrange(0,min(len(couple_sums),lastInd)):
    if lastInd > len(couple_sums):
        pSum(currSum+couple_sums[i],i)
    elif compatible(cInds[i],cInds[lastInd]):
        pSum(currSum+couple_sums[i],i)
pSum(0,len(couple_sums)+10)
#print cInds
print s+1

#for i in xrange(len(couple_sums)):
 #if couple_sums[i] > cap:
  # break
 #tset = set()
 #tset.add(couple_sums[i])
 #for s in sums:
  # t = s+couple_sums[i]
   #if t > cap:
    # continue
   #tset.add(s+couple_sums[i])
 #sums = sums.union(tset)
#print sums  
#print sum(sums)
