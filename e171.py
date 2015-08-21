from itertools import combinations

d = 20
mod = 10**9
fact = [1]
for i in xrange(1,d+1):
 fact.append(fact[-1]*i)

C = lambda n,k : fact[n]/fact[k]/fact[n-k]
one_sum = [0] #k-th member is the sum of all nums < 10^d with k digits 1, and the rest 0
geo = ((10**d -1)/9) % mod
for i in xrange(1,d+1):
 one_sum.append(geo*C(d-1,i-1))
print one_sum

squares = set(i*i for i in xrange(int((9*9*d)**.5)+1))
s = 0
cases=0
#Iterate over partitions of d into 10 parts
#So 9 separators are needed
for c in combinations(range(d+9),9):
  sq_sum = 81*(d+8-c[-1]) #count the 9 digits
  for i in xrange(1,9):
    sq_sum += (c[i]-c[i-1]-1)*i*i
    
  if sq_sum not in squares:
    continue
  cases += 1
  c  = list(c) + [d+9]
  n = [c[0]]
  tot = fact[d]/fact[n[-1]]
  for i in xrange(1,10):
    n.append(c[i]-c[i-1]-1)
    tot /= fact[n[-1]]
  for i in xrange(1,10):
    s = (s + (tot/C(d,n[i])) * (one_sum[n[i]]) * i) % mod

print "Cases: %d" % cases  
print "Sum %d" % s    
    
    
  


