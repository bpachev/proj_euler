with open("/home/benjamin/gmp/gmp-1.3.2/cands.txt") as fp:
 ns = []
 for line in fp:
   t = line.strip().split(" ")[-1]
   ns.append(int(t))
   
m = 49580620131241271
sav = 840*3
b = 4.9615079365079364  
print "Its total: %d" % int((ns[-1]-m/b) / (sav))
days = ((ns[-1]-m/b) / (sav*3600*24*(10**7/11.)) )
print "Days total %f " % days
print "Minutes total %f" % (days * (60*24)) 

