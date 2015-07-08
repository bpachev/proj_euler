s = 0
cap = 10**6
mod = 1000000007
for i in xrange(1,cap+1):
  t = 1-i**2
  s = (s + t*(pow(t,cap,mod)-1)*(pow(t-1,mod-2,mod))) % mod

print s
