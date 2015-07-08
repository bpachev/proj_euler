def collatz_root(mask):
  a = 1
  b = 0
  for f in mask:
    #multiplication by 2
    if f == 1:
      a = 2*a
      b = 2*b
    # (x-1)/3
    if f == 0:
      a = a/3.
      b = (b-1)/3.
  if a == 1:
    return 0 
  return -b/(a-1)

p_of_2 = set([2**k for k in xrange(50)])

def coll_len(x):
  global p_of_2
  if x in p_of_2:
    return 0
  if x % 2 == 0:
    return 1 + coll_len(x/2)
  else:
    return 1 + coll_len(3*x+1)

paths = []

def max_root(x,depth,a, b,path):
  global paths
  paths.append(path+[x])
  if depth < 0:
    return -2
  
  if a == 1:
    curr_root = -2
  else:
    curr_root = -b/(a-1)

  if x % 2 == 0 and x % 3 == 1:
    return max( (curr_root,max_root((x-1)/3,depth-1,a/3.,(b-1)/3.,path+[0]),max_root(2*x,depth-1,2*a,2*b,path+[1]) ) )
  else:
    return max( (curr_root,max_root(2*x,depth-1,2*a,2*b,path+[1])) )


max_root(20,17,1,0,[])

for p in paths:
  c = collatz_root(p)
  if c > 30:
    print c
    print p

#for x in xrange(3, 100):
 # m = max_root(x,20-coll_len(x),1,0,[])
 # if m > 30 and m > x:
  #  print str(m) + " " + str(x) + " " +  str(coll_len(x))
#for x in xrange(1,19):
 # new_families = []
  #for f in families:
   # if f[-1] == 1:
    #  new_families.append(f + [1])
     # new_families.append(f + [0])
    #if f[-1] == 0:
     # new_families.append(f + [1])
#  families = new_families
 # for s in families:
  #  r = collatz_root(s)
   # if r >= 15 and r <= 115 and x < 15:
    #  print r
     # print s

#print collatz_root([1,0,1,0,1,0])
