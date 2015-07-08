
def tuple_prod(T):
  prod = 1
  for t in T:
    prod = prod*t
  return prod

def inner_prod(u,v):
  r = 0
  for i, x in enumerate(u):
    r += x*v[i]
  return r

def EEA(a,b):
  '''
  RETURNS r, s, t
  r -- gcd(a,b)
  s and t satisfy as + bt = d
  '''
  an, bn = a, b
  if b > a:
    an, bn  = b, a
  
  s_prev, t_prev, s, t, r_curr, r_next = 1,0, 0, 1, an, bn
  while r_next:
    r_old, t_old, s_old = r_next, t, s
    q, r_next = r_curr/r_next, r_curr % r_next 
    r_curr = r_old
    t, s = t_prev - q*t, s_prev - q*s
    s_prev, t_prev = s_old, t_old  
 
  if a > b:
    return r_curr, s_prev, t_prev
  else:
    return r_curr, t_prev, s_prev

  
def Lagrange_decomp(x, M):
  '''
  x is an integer
  M is a tuple of pairwise relatively prime integers
  RETURN -- L a tuple satisfying x = L1 + . . . + Ln mod m1*m2*...*mn 
  '''
  
  L = []
  p = tuple_prod(M)
  for m in M:
    q = p/m
    r, s, t = EEA(q,m)
    L.append(x*q*s % p)
  
  return tuple(L)

def Lagrange_cr(R, M):
  '''
  R is the tuple of remainders mod mi
  M is a tuple of pairwise relatively prime integers
  RETURN -- x, the solution to the Chinese Remainder Problem
  '''
  X = 0
  p = tuple_prod(M)
  for i, m in enumerate(M):
    q = p/m
    r, s, t = EEA(q,m)
    X += R[i]*q*s
  return X % p

def Newton_Garner(R, M):
  '''
  R is the tuple of remainders mod mi
  M is a tuple of pairwise relatively prime integers
  RETURN -- x, the solution to the Chinese Remainder Problem
  '''
  B = [R[0]] #list of b's
  P = [1] #list of products 
  n = len(M)
 
  for i, m in enumerate(M):
    P.append(m*P[i])
    if i == n-1:
      return inner_prod(B,P) % P[-1]
    else:
      print B
      print P
      s = EEA(P[i], M[i+1])[1]
      B.append(s*(R[i+1] - inner_prod(B,P)))


#print Lagrange_cr((9,8,3),(19,18,17))       
#print Newton_Garner((9,8,3),(19,18,17))

