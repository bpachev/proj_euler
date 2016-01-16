from matplotlib import pyplot as plt
import numpy as np
l=30.403243784
u = lambda x : 2**(l-x*x)*1e-9
x0=-1

r =[]
for i in xrange(10000):
 x0=u(x0)
 r.append(x0)
r=np.array(r)
np.set_printoptions(precision=15)
print r[::2]+r[1::2]
