#My Python code runs in just uder 29 seconds. We have that n!/(k!*(n-k)!) * (k-1)! = n*(n-1) * . . . * (n-k+1) /k, so there is no need to compute and store factorials. The remaining coefficient can b computed on the fly.
#[code]
n = 12344321
mod = 135707531
s = n*(n-1)*pow(n-2,n-1,mod) % mod #total num orphans
coeff = n
for k in xrange(2,n-1):
  coeff = (coeff * (n-k+1)) % mod #n!/(n-k)!
  s = ( s + coeff*pow(k,mod-2,mod)*pow((n-k-1),(n-k),mod)) % mod #don't forget 1/k
print s
#[/code]
