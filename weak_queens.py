import numpy as np
from numpy import bitwise_xor,count_nonzero

n = 14
mask = [2**r for r in xrange(n)]
board = np.zeros((n,n),dtype=int)
diags = {o:np.diagonal(board,o) for o in xrange(-(n-1),n)}

def backtrack(arr,qs=[],r=0):
	if r>=arr.shape[0]:
		return 1
	s=0
	for i in xrange(n):
		if arr[r][i]==0:
			f=0
			for q in qs:
				if q[1]==i or r-q[0]==abs(i-q[1]):
					f=1
					break
			if not f:
				qs.append((r,i))
				s+=backtrack(arr,qs,r+1)
				qs.pop()
	return s

def backtrackgen(rows,qs=[],r=0,strength=0):
#	print "hi",qs,strength,r,rows,qs[max(r-strength,0):]
	if r>=rows:
		yield tuple(qs)
		return
	s=0
	for i in xrange(n):
			f=0
#			print qs[max(r-strength,0):]
			for j in xrange(max(r-strength,0),r):
				q = qs[j]
				if q==i or r-j==abs(i-q):
					f=1
					break
			if not f:
				qs.append(i)
				for q in backtrackgen(rows,qs,r+1,strength):
					yield q
				qs.pop()

def fsm_sol(n,w):
	statedict = {}
	transdict = {}
	for ql in backtrackgen(rows=w+2,strength=w):
		s1,s2 = ql[:-1],ql[1:]
		statedict[s1] = 1
		if s1 in transdict:
			transdict[s1].append(s2)
		else:
			transdict[s1] = [s2]
	for i in xrange(n-w-1):
		tdict = statedict.copy()
		for s1 in statedict:
			statedict[s1] = 0
		for s1 in transdict:
			for s2 in transdict[s1]:
				if s2 not in statedict:
					statedict[s2] = 0
				statedict[s2] += tdict[s1]
	return sum([statedict[s] for s in statedict])

print sum([fsm_sol(n,i) for i in xrange(4)])

def queens(row,w):
 s = 0
 if row==n-1:
  return n-count_nonzero(board[row,:])

 for i in xrange(n):
  if board[row][i]==0:
   #set bits as under attack from row (row)
   endr = min(row+w+1,n)
   board[row:endr,i]=bitwise_xor(board[row:min(row+w+1,n),i],mask[row])
   #diagonal
   for t in xrange(1,min(n-i,n-row,w+1)):
    board[row+t][i+t] ^= mask[row]
   for t in xrange(1,min(i+1,n-row,w+1)):
    board[row+t][i-t] ^= mask[row]
   s += queens(row+1,w)
   #clear bits, reset
   for t in xrange(1,min(n-i,n-row,w+1)):
    board[row+t][i+t] ^= mask[row]
   for t in xrange(1,min(i+1,n-row,w+1)):
    board[row+t][i-t] ^= mask[row]
   board[row:endr,i]=bitwise_xor(board[row:min(row+w+1,n),i],mask[row])

 return s
def solve(n):
 tot = n**n
 for w in xrange(1,n):
  inc = queens(0,w)
  print inc,w
  tot += inc
 print tot-n**n,tot

#solve(n)
def recur(n):
 pass