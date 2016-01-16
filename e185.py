import sys

if len(sys.argv) <=1:
 print "Usage [infile]"


def parse_infile():
 res = []
 f=open(sys.argv[1],"r")
 for line in f:
  l=line.split(" ")
  guess=l[0]
  correct=int(l[1][1:])
  res.append([guess,correct])
 return res


d_list = map(str,range(10))

def find_sol(s,g,i,l):
 global d_list
 """
 s -- the current guess
 g -- the list of guesses and 
 i -- the current number of steps
 l -- the total number of steps
 """
 
 if i==l:
  print "".join(s),g
  return True
 
 for d in d_list:
  fail=False  
  for el in g:
   if d==el[0][i]:
    el[1]-=1
    #if too many things are correct, or if there's no possible way enough things can be correct
    if el[1] <0:
     fail=True
   if l-i-1<el[1]:
    fail=True
     
  
  #if adding d creates no inconsistencies   
  if not fail:
   s[i] = d 
   if find_sol(s,g,i+1,l):
    return True
 
  #restore things to previous state
  for el in g:
   if d==el[0][i]:
    el[1]+=1
 return False
  

def row_sol(s,g,depth):
 global inds
 if depth == len(g):
  print "".join(s)
  return s
 
 #iterate over all combinations of clues for g
 nclues = g[depth][1]
 if not nclues:
   return row_sol(s,g,depth+1)
 
 for c in combinations(inds,nclues):
  

res = parse_infile()
l=len(res[0][0])
s=[-1]*l
inds = range(l)
row_sol(s,res,0)

