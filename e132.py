import proj_euler as pe

cap = 2*10**5
pcap = 2*10**5
n = 10**9
mask = pe.mark_primes(pcap)
cache = []
pDivs = {}
i = 1
e1 = 0
while i < cap:
  j = 1
  e2 = 0
  cache.append([])
  while j*i < cap:
    t = j*i
    cache[e1].append(t)
    for k in xrange(t,cap,t):
      if pe.is_prime(k+1,pcap,mask):
        if k+1 not in pDivs:
          pDivs[k+1] = [t]
        else:
          pDivs[k+1].append(t)
      
    j *= 5
    e2 += 1
  
  i *= 2
  e1 += 1

s = 0
num_found = 0
m = 40

for p in sorted(pDivs):
  if p in [2,5,3]:
    continue
  for div in sorted(pDivs[p]):
    if pow(10,div,p) == 1:
#      print p,div
      if n % div == 0:
        print p
        num_found += 1
        s += p
        break
      else:
        break
  if num_found == m:
    print "answer: %d" % s
    break
print "TOTAL NUM FOUND %d" % num_found         
        
    
    
