def savings(r1,r2):
  '''
  The savings in length when two spheres of radius r1 and r2 are placed in a pipe of radius 100.
  It is assumed that 25 < r1,r2 <= 50 
  '''
  T = r1+r2
  return T - (T*T-(100-T)**2)**.5

