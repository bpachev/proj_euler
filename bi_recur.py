import numpy as np

def x_k(k,mod = pow(2,60)):
  if k <= 1:
    return k
  k_coeff = 1
  k2_coeff = 0

  while not k == 1:
    if k % 2:
      temp = k_coeff
      k_coeff = k2_coeff + 2*k_coeff
      k2_coeff = 3*temp
    else:
      temp = k_coeff
      k_coeff = k2_coeff + 3*k_coeff
      k2_coeff = 2*temp
    k = k / 2

  return k_coeff % mod

def half_A(n,k, lower, upper):
    res = A(n, 2*k, lower, upper)
    if res <= upper:
        res = max(res, A(n, 2*k+1, max(lower, res), upper))
    return res

mod = 2**60
def A(n,k, lower = 0, upper = mod):
    if k >= n: return x_k(k)
    elif k >= (n-1) / 2: return mod - 1 - max(A(n, 2*k), A(n, 2*k+1))
    else:
        first = half_A(n, 2*k, lower, upper)
        if first >= lower:
            first = min(first, half_A(n, 2*k+1, lower, min(upper, first)))
        return first
print A(10**12, 1)
def range_winner(x1,x2,cutoff,base = 0,mod = pow(2,60)):
  '''
  Assume the bottom of the tree is maxes.
  '''

  num_contestants = x2 - x1
  level = np.arange(0,num_contestants)
  indices = np.arange(0, num_contestants)
  for i,x in enumerate(level):
    if (x+x1)/2 < cutoff:
      level[i] = x_k(x+x1)
    else:
      level[i] = mod - 1 - x_k((x+x1)/2)

  j = 0
  while num_contestants > 1:
    num_contestants = num_contestants / 2
    #maxes
    if j % 2 == base:
      for k in xrange(num_contestants):
        if level[indices[2*k]] > level[indices[2*k+1]]:
          indices[k] = indices[2*k]
        else:
          indices[k] = indices[2*k + 1]

    #mins
    else:
      for k in xrange(num_contestants):
        if level[indices[2*k]] < level[indices[2*k+1]]:
          indices[k] = indices[2*k]
        else:
          indices[k] = indices[2*k + 1]
    j += 1
  return indices[:num_contestants] + x1

def range_max(x1,x2):
  mx = 0
  mn = 2**60
  ix = -1
  i_min = -1
  for i in xrange(x1,x2):
    t = x_k(i)
    if t > mx:
      mx = t
      ix = i
    if t < mn:
      mn = t
      i_min = i
  return mx, mn, bin(i_min), bin(ix)

#print range_max(2**40,2**40 + 8)
#print range_max(2**40 + 8,2**40 + 2*8)


#print x_k(range_winner(2**17,2**18,10**5)[0])
