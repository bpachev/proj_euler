import numpy as np

def tribbo_period(mod):
  t = [0,0,1]
  i = 3
  while True:
    temp = t[2]
    t[2] = (t[2] + t[1] + t[0]) % mod
    t[0] = t[1]
    t[1] = temp
    if t[0] == 0 and t[1] == 0 and t[2] == 1:
      return i
    i += 1

def special_tribbo_period(mod):
  V = np.zeros(3).astype(int)
  W = np.zeros(3).astype(int)
  curr_trib = np.zeros(12).astype(int)
  past_trib = np.zeros(12).astype(int)
  past_trib[-1] = 0
  past_trib[-2] = 1
  past_trib[-3] = -1

  i = 1
  while True:
    curr_trib[0] = (past_trib[-1] + past_trib[-2] + past_trib[-3]) % mod
    curr_trib[1] = (curr_trib[0] + past_trib[-1] + past_trib[-2]) % mod
    curr_trib[2] = (curr_trib[1] + curr_trib[0] + past_trib[-1]) % mod
    for j in xrange(3,12):
      curr_trib[j] = (curr_trib[j-1] + curr_trib[j-2] + curr_trib[j-3] ) % mod
    V[0] = curr_trib[0] - curr_trib[1]
    V[1] = curr_trib[2] + curr_trib[3]
    V[2] = curr_trib[4]*curr_trib[5]
    W[0] = curr_trib[6] - curr_trib[7]
    W[1] = curr_trib[8] + curr_trib[9]
    W[2] = curr_trib[10]*curr_trib[11]
    if V[0] == -1 and V[1] == 3 and V[2] == 28 and i > 1:
      return i

    if W[0] == -1 and W[1] == 3 and W[2] == 28 and i > 1:
      return i
    curr_trib, past_trib = past_trib, curr_trib
    i += 1




print tribbo_period(10**7)
