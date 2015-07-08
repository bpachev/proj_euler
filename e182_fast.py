import proj_euler as pe

q = 1009
p = 3643

qdivs = [1  ,  2  ,  3  ,  4  ,  6  ,  7  ,  8  ,  9  ,  12  ,  14  ,  16  ,  18  ,  21  ,  24  ,  28  ,  36  ,  42  ,  48  ,  56  ,  63  ,  72  ,  84  ,  112  ,  126  ,  144  ,  168  ,  252  ,  336  ,  504  ,  1008]


pdivs = [1  ,  2  ,  3  ,  6  ,  607  ,  1214  ,  1821  ,  3642]
pdivDict = {n : 0 for n in pdivs}
qdivDict = {n : 0 for n in qdivs}

for m in xrange(p):
  for d in pdivs:
    if m == pow(m,d+1,p):
      pdivDict[d] += 1

for m in xrange(q):
  for d in qdivs:
    if m == pow(m,d+1,q):
      qdivDict[d] += 1

print pdivDict
print qdivDict
print pdivs
print qdivs
print "Completed initialization."
s = 0
m = 10**9
for e in xrange((p-1)*(q-1)):
  if e%2 and e%3 and e%7 and e % 607:
    tm = (1 + pe.egcd(e-1,p-1)[0]) * (1 + pe.egcd(e-1,q-1)[0])
    if tm < m:
      m = tm
      s = e
    elif tm == m:
      s += e

print "min " + str(m)
print "sum " + str(s)

        
