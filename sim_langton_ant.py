import numpy as np
from matplotlib import pyplot as plt

maxN = 1000

grid = np.zeros((maxN,maxN),dtype=int)
dirs = [(1,0),(0,-1),(-1,0),(0,1)]

def sim(x,y,d,niter):
  global maxN,dirs,grid
  for i in xrange(niter):  
    if max(abs(x),abs(y)) >= maxN:
      return
    new_d = (d + (-1)**(grid[x,y])) % 4
    new_dir = dirs[new_d]  
    grid[x,y] = grid[x,y]^1
    x,y = x+new_dir[0],y+new_dir[1]
    d = new_d
  return


sim (500,500,0,11064)
#plt.imshow(grid)
#plt.show()
print np.sum(np.sum(grid))
