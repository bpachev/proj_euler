from proj_euler import shanks_factorize,MillerRabin

def f(n):
  f = shanks_factorize(n)
  return max(f.keys())

def g(n):
  return sum([f(n+i) for i in xrange(9)])
  
with open("/home/benjamin/gmp/gmp-1.3.2/cands.txt") as fp:
 cands = []
 ns = []
 for line in fp:
   t = line.strip().split(" ")[-1]
   ns.append(int(t))
   cands.append(g(int(t)))
#   print t, cands[-1]

sav = 840*3
b = 4.9615079365079364
m =  max(cands)
print m   
print "Its total: %d" % int((ns[-1]-m/b) / (sav))
print "Days total %f " % ((ns[-1]-m/b) / (sav*3600*24*(10**7/11.)) ) 

