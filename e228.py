from proj_euler import egcd

def minkowski_verts(start,stop):
  fracs = set()
  for i in xrange(start,stop+1):
    for j in xrange(1,i):
      d = egcd(i,j)[0]
      fracs.add((j/d,i/d))
  #the 1 is to account for sides with polar angle of 0/90 degrees
  return 1 + len(fracs)

print minkowski_verts(1864,1909)
