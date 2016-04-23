
def M(m,k,s,n):
  print n
  if n > m:
    return n - s
  else:
    return M(m,k,s,M(m,k,s,n+k))


def linear_M(m,k,s,n):
    calls = 1
    state = n
    print calls, state
    while calls > 0:
        if state > m:
            state -= s
            calls -= 1
        else:
            calls += 1
            state += k
        print calls, state
    return state

def S_slow(m):
    tot = 0
    for d in xrange(1,m/2+1):
        for k in xrange(1, m/d):
            tot += m*d - k*d**2 + d*(d+1) / 2
    return tot

def S_fast(m):
    tot = 0
    for d in xrange(1,m/2+1):
        f = m/d-1
        tot += f * (m*d + d*(d+1) / 2) - d**2 * f*(f+1) / 2
    return tot


print S_fast(1000000)
