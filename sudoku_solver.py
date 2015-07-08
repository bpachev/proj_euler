import numpy as np


def inc_pos(i,j):
  if i == 8:
    if j == 8:
      return 9,9
    else:
      return i,j+1
  else:
    if j == 8:
      return i+1,0
    else:
      return i,j+1

def dec_pos(i,j):
  if i == 0:
    if j == 0:
      print "Unsolvable"
      return -1,-1
    else:
      return i,j-1
  else:
    if j == 0:
      return i-1,8
    else:
      return i,j-1
  
def compatible(i,j,b):
  v = b[i,j]
  if not v:
    return False
  
  #check if anything in the row conflicts
  for k in xrange(9):
    if b[i,k] == v and not k == j:
      return False
  #check if anything in the column conflicts
  for k in xrange(9):
    if b[k,j] == v and not k == i:
      return False

  #check if anything in the box conflicts
  for k in xrange(3*(i/3),3*(i/3)+3):
    for l in xrange(3*(j/3),3*(j/3)+3):
      if b[k,l] == v:
        if not k == i or not l == j:
          return False
   
  return True

def solve_sudoku(board,miter=50000000):
  b = np.copy(board)
  #initial position
  n = 0
  i = 0 
  j = 0
  d = 1 #forward
  while True:
    if i == 9 and j == 9:
      return b
    if n == miter:
      print "Exceeded Maxiter"
      return b
    #Can Not Change the Initial Clues!
    if board[i,j]:
      if d == 1:
#        print "On " + str((i,j))  
        i,j = inc_pos(i,j)
#        print "Advanced to " + str((i,j))
        n += 1
        continue
      else:
#        print "On " + str((i,j))  
        i,j = dec_pos(i,j)
#        print "Backed to " + str((i,j))
        n += 1
        continue
     
    else:
      if d == -1:
        b[i,j] += 1
      while not compatible(i,j,b):
        b[i,j] += 1
        if b[i,j] == 10:
          break
      if b[i,j] < 10:
#         print "On " + str((i,j)) + " set to " + str(b[i,j])
         d = 1 #we may have been backtracking, so need to go forward now
         i,j = inc_pos(i,j)
         n += 1
      else:
#         print "On " + str((i,j)) + " backtracked"      
         d = -1 #backtrack 
         b[i,j] = 0 #reset
         i,j = dec_pos(i,j)
         n += 1
         continue
         






fname = "p096_sudoku.txt"
s = 0
nb = 0
s_arr = []
with open(fname) as fp:
  for line in fp:
    line = list(line.strip())
    if line[0] == 'G':
      if len(s_arr):
        nb += 1
        print "On " + str(nb)
        sol = solve_sudoku(np.array(s_arr))
        s += 100*sol[0,0] + 10*sol[0,1] + sol[0,2]
        s_arr = []
    else:
      s_arr.append(map(int,line))
      
sol = solve_sudoku(np.array(s_arr))
s += 100*sol[0,0] + 10*sol[0,1] + sol[0,2]
print s

