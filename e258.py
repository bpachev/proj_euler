import proj_euler as pe
import numpy as np

off = 2000
n = 10**18

T = np.zeros((off,off))

T[0,off-2] = 1
T[0,off-1] = 1
for i in xrange(1,off):
  T[i,i-1] = 1
print "Done initializing."
I = np.ones(off)
mods = [2,5,859,2339]
for m in mods:
 print "F("+str(n)+") mod "+str(m)
 print pe.matrix_mod_exp(n-off+1,T,I,m)




