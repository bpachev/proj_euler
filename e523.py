
n = 30
fact = [1]
for i in xrange(1,n+1):
 fact.append(i*fact[-1])
 
comb = lambda r,k : fact[r]  / fact[r-k] / fact[k]

tot = 0.
#over number of open slots before elem
for pos in xrange(1,n):
 #over elem
 for elem in xrange(1,n+1):
    #over number of elements before elem and less than it
    for num in xrange(0, min(pos,elem)):
      tot += comb(elem-1,num) * comb(n-elem,pos-num) * 2**num * fact[pos] * fact[n-pos-1]

print tot
print tot / (fact[n]*1.)
