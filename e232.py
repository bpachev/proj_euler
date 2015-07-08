
#Probablility of Player 2 winning GIVEN that it is her turn, and the score is like so
def P2(n,k):
  global cache
  global pows2
  global cap
  if k >= cap:
    return 1
  if n >= cap:
    return 0    
  if (n,k) in cache:
    return cache[(n,k)]
  i = 1
  m = 0.
  while True:
    t = pows2[i-1]/(pows2[i-1]+1.) * (1./pows2[i] * (P2(n,k+pows2[i-1]) + P2(n,k+pows2[i-1])) + (1.-1./pows2[i]) * P2(n+1,k))
    if t > m:
      m = t
    if k + 2**i >= cap:
      break
    i += 1
  cache[(n,k)] = m
  return m

#Probability of Player 1 winning GIVEN that it is his turn
def P1(n,k):
  return 0.5 * (P2(n+1,k) + P2(n,k))

pows2 = []
cache = {}
for i in xrange(9):
  pows2.append(2**i)

cap = 100

print P2(0,0)
