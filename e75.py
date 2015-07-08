import numpy as np

def generate_pythag_triples(cap = 1500000):
  hcf = lambda n1, n2: n1 if n2 == 0 else hcf( n2, n1 % n2 )
  mask = np.zeros(cap+1)
  for m in xrange(1,int(cap**0.5)+1):
    for n in xrange(1,min(m,int((cap-m**2)**0.5)+1)):
      tmp = 2*m*(m+n)
      if tmp <= cap and hcf(m,n) == 1 and (m - n) % 2 == 1:
        for k in xrange(1,cap/tmp + 1):
          mask[k*tmp] += 1
  print sum(mask[(mask == 1)])

generate_pythag_triples()
