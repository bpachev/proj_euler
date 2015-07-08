from itertools import permutations

n = 11
k = 2011
m = [[1,0]]
m_new = []

for i in xrange(2,n):
  m_new = []
  for arr in m:
    t = [e +1 for e in arr]  
    for a_pos in xrange(1,i):
      nt = t[-1:a_pos-1:-1] + [0] + t[:a_pos]
      m_new.append(nt)
  m = m_new
ans = sorted(m)[k-1]
print "".join(map(lambda x : chr(ord('A') + x),ans))
