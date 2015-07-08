import numpy as np

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def sum_class(d,prefix,rem,digits,base = 10**6,mod = 123454321):
  if d +1 < 0:
    return 0 
  invb = modinv(base-1,mod)
  c = (prefix * 10**digits * invb )
  return (((pow(base, d+1,mod) - 1 ) * invb * base - d - 1)* c + (d+2)*rem ) % mod

def v_n(n_div_d,prefix,rem,digits,base = 10**6,mod = 123454321):
  invb = modinv(base-1,mod)
  c = ((10**digits*prefix) % mod *invb) % mod
  return (c*(pow(base,n_div_d,mod) - 1) + rem) % mod
  

def clock_sum(n,mod = 123454321):
  period = 15
  rem = np.array([0,1,2,3,4,32,123,43,2123,432,1234,32123,43212,34321,23432])
  digits = np.array([0,1,1,1,1,2,3,2,4,3,4,5,5,5,5])
  prefixs = np.array([123432,123432,234321,343212,432123,321234,123432,432123,212343,432123,123432,321234,432123,343212,234321])
  k = n % period
  d = n / period
  
  res = 0
  #sum over equivalence classes modulo period
  for i in xrange(period):
    if i <= k: 
      res = (res + sum_class(d-1,prefixs[i],rem[i],digits[i],mod = mod)) % mod  
    else:
      res = (res + sum_class(d-2,prefixs[i],rem[i],digits[i],mod = mod)) % mod

  return res

print clock_sum(10**14)   
