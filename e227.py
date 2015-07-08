#Benjamin Alexander Pachev benjaminpachev@gmail.com
import numpy as np
import scipy.linalg as la


cap = 100
n = cap/2 # n states
#if zero players separate the dice, the game is over and the number of turns left is zero, so don't need to solve for that 
T = np.zeros((n,n))

for i in xrange(2,n-2):
  T[i,i] = 0.5 #Both dice don't move 4*4/36 + both move in same direction 2/36 = 18/36
  T[i,i+1] = 8./36 #One moves away
  T[i,i-1] = 8./36 #One moves closer
  T[i,i+2] = 1./36 #both move apart each other
  T[i,i-2] = 1./36 #both move together

#Seperated by one
T[0,0] = 0.5 + 1./36 #If both move together, they swap places and remain one unit apart
T[0,1] = 8./36 #One moves apart
T[0,2] = 1./36 #Both apart

#One more than min distance
T[1,0] = 8./36
T[1,1] = 0.5
T[1,2] = 8./36
T[1,3] = 1./36
#If both move toward eachother, the distance becomes zero and the game ends

#Max distance apart, can't get further
T[n-1, n-1] = 0.5
T[n-1,n-2] = 16./36
T[n-1,n-3] = 2./36

#One less than max distance
T[n-2,n-1] = 8./36
T[n-2,n-2] = 0.5 + 1./36
T[n-2,n-3] = 8./36
T[n-2,n-4] = 1./36

print la.solve(np.identity(n) - T,np.ones(n))
