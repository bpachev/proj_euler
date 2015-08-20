d = 18
fact = [1]
for i in xrange(1,d+1):
 fact.append(fact[-1]*i)
s = 0
for n3 in xrange(d/3+1):
 for n2 in xrange((d-3*n3)/2+1):
  n1 = d - 3*n3-2*n2
  if n3+n2+n1 > 10:
   #not more than 10 digits
   continue
  t = fact[18]
  if n3:
   t /= (fact[3]**n3)
  if n2:
   t /= (fact[2]**n2)
  s += t*(fact[10]/fact[n3]/fact[n2]/fact[n1]/fact[10-n1-n2-n3])
print (9*s)/10
