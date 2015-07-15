import proj_euler as pe

pcap = 2*10**5
d = 19
cap = 10**12
pow10 = [10**i for i in xrange(d+2)]
primes = pe.primes_and_mask(pcap)[0]

def prime_proof(t,st):
  global pow10
  digs = len(st) #number of digits
  for i in xrange(digs):
    for j in xrange(10):
      temp = t + (j-int(st[-i-1]))*pow10[i]
      if pe.MillerRabin(temp):
        return False
  return True


pp_squbes = []
for p in primes:
  if p > cap/8:
    break
  for q in primes:
    if q == p:
      continue
    t = p*p*q**3
    if t > cap:
      break
    st = str(t)
    if st.find("200") >= 0:
      if prime_proof(t,st):
        pp_squbes.append(t)
#        print t
ind = 200
l = len(pp_squbes)
print "length %d" % l
if l >= ind:
  print sorted(pp_squbes)[ind-1] 

