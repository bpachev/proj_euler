import scipy as sp
import numpy as np
import scipy.linalg as la
from sympy import Matrix,zeros,eye,N
#import mpmath as mp
from numpy.linalg import matrix_power

#the laplacian matrix of the graph of a wxh grid
def grid_laplacian(w,h):
  n = w*h
  k1,k2 = min(w,h),max(w,h)
  L = np.zeros((n,n)) 
  for i in xrange(n):
    q,r = divmod(i,k1)
    L[i,i] = 2
    if r:
     L[i,i-1] = -1
     if r <k1-1:
      L[i,i] += 1
      L[i,i+1] = -1
    else:
     L[i,i+1] = -1
    if q:
      L[i,i-k1] = -1
      if i/k1 < k2-1:
        L[i,i] += 1
        L[i,i+k1] = -1
    else:
     L[i,i+k1] = -1
    
  return L

#the transfer matrix of the augmented coafactor matrix of the Laplacian of a wxh grid
def grid_transfer_mat(w,h):
  k1,k2 = min(w,h),max(w,h)
  T1 = np.zeros((2*k1,2*k1),dtype=np.float128)
  T1[k1:,:k1] = np.eye(k1,dtype=np.float128)
  T1[:k1,k1:] = -1*np.eye(k1,dtype=np.float128)
  for i in xrange(1,k1-1):
    T1[i,i] = 4
    T1[i,i+1] = -1
    T1[i,i-1] = -1
  #Set boundary values
  T1[0,0] = 3
  T1[0,1] = -1
  T1[k1-1,k1-2] = -1
  T1[k1-1,k1-1] = 3  
#  print T1
  
  T2 = np.zeros((2*k1,2*k1),dtype=np.float128)
  T2[k1:,:k1] = np.eye(k1,dtype=np.float128)
  T2[:k1,k1:] = np.eye(k1,dtype=np.float128)
  T2[:k1,:k1] = T1[:k1,:k1] - np.eye(k1,dtype=np.float128)
#  print T2
  
  T3 = np.zeros((2*k1,2*k1),dtype=np.float128)
  T3[:k1-1,:k1-1] = T2[:k1-1,:k1-1]
  T3[k1-1,k1-1] = 1
  T3[k1:,:k1] = np.eye(k1,dtype=np.float128)
  T3[:k1-1,k1:2*k1-1] = -1*np.eye(k1-1,dtype=np.float128)
#  print T3
  return Matrix(T3)*Matrix(T1)**(k2-2)*Matrix(T2)
 
def grid_transfer_mat_safer(w,h):
  k1,k2 = min(w,h),max(w,h)
  T1 = np.zeros((2*k1,2*k1),dtype=int)
  T1[k1:,:k1] = np.eye(k1,dtype=int)
  T1[:k1,k1:] = -1*np.eye(k1,dtype=int)
  for i in xrange(1,k1-1):
    T1[i,i] = 4
    T1[i,i+1] = -1
    T1[i,i-1] = -1
  #Set boundary values
  T1[0,0] = 3
  T1[0,1] = -1
  T1[k1-1,k1-2] = -1
  T1[k1-1,k1-1] = 3  
#  print T1
  
  T2 = np.zeros((2*k1,2*k1),dtype=int)
  T2[k1:,:k1] = np.eye(k1,dtype=int)
  T2[:k1,k1:] = np.eye(k1,dtype=int)
  T2[:k1,:k1] = T1[:k1,:k1] - np.eye(k1,dtype=int)
#  print T2
  
  T3 = np.zeros((2*k1,2*k1),dtype=int)
  T3[:k1-1,:k1-1] = T2[:k1-1,:k1-1]
  T3[k1-1,k1-1] = 1
  T3[k1:,:k1] = np.eye(k1,dtype=int)
  T3[:k1-1,k1:2*k1-1] = -1*np.eye(k1-1,dtype=int)
#  print T3
  return Matrix(T3)*Matrix(T1)**(k2-2)*Matrix(T2)

def new_transfer(w,h,prec = 600):
  k1,k2 = min(w,h),max(w,h)
  T1 = zeros((2*k1,2*k1))
  T1[k1:,:k1] = eye(k1)
  T1[:k1,k1:] = -1*eye(k1)
  for i in xrange(1,k1-1):
    T1[i,i] = N(4,prec)
    T1[i,i+1] = N(-1,prec)
    T1[i,i-1] = N(-1,prec)
  #Set boundary values
  T1[0,0] = N(3,prec)
  T1[0,1] = N(-1,prec)
  T1[k1-1,k1-2] = N(-1,prec)
  T1[k1-1,k1-1] = N(3,prec)  
#  print T1
  
  T2 = zeros((2*k1,2*k1))
  T2[k1:,:k1] = eye(k1)
  T2[:k1,k1:] = eye(k1)
  T2[:k1,:k1] = T1[:k1,:k1] - eye(k1)
#  print T2
  
  T3 = zeros((2*k1,2*k1))
  T3[:k1-1,:k1-1] = T2[:k1-1,:k1-1]
  T3[k1-1,k1-1] = N(1,prec)
  T3[k1:,:k1] = eye(k1)
  T3[:k1-1,k1:2*k1-1] = -1*eye(k1-1)
#  print T3
  return T3*T1**(k2-2)*T2

w,h = 100,500
print new_transfer(w,h)[:w,:w].det()
#L = grid_laplacian(w,h)
#print L
#T = grid_transfer_mat(w,h)
#print T
#print "Got Matrix"

#M = Matrix(T[:w,:w])
#print M.det()
#res = str(grid_transfer_mat_safer(w,h)[:w,:w].det())
#print len(res)
#print res[:5]

