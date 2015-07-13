import proj_euler as pe

cap = 10**5
mask = pe.mark_primes(cap)

tiles = [1]
st = 2
layer = 1
mLayers = 100000

def p_sum(d):
  s = 0
  for i in xrange(3):
    s += pe.is_prime(d[i],cap,mask)
  return s
  
for layer in xrange(1,mLayers+1):
  #check 12-oclock
  d = [6*layer +1, 6*layer -1, 6*(2*layer+1)  - 1]
  if p_sum(d) == 3:
    tiles.append(st)


  d_start = [6*layer,6*layer+1,6*layer+2,6*(layer-1)-1]
  for i in xrange(1,6):
    if p_sum(d_start) == 3:
      tiles.append(st + i*layer)
    for j in xrange(4):
      d_start[j] += 1
    
  d_new = [d[1],6*(layer-1)+d[1],d[2]-d[1]-1]
  if p_sum(d_new) == 3:
   tiles.append(st + 6*layer - 1)
#  print d_new
#  print d
#  print layer
  st += 6*layer
print len(tiles)
if len(tiles)>2000:
  print tiles[2000]
  
  
  
