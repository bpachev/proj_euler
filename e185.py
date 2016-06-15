import sys
from itertools import combinations
import numpy as np

if len(sys.argv) <=1:
 print "Usage [infile]"


def parse_infile():
 res = []
 f=open(sys.argv[1],"r")
 for line in f:
  l=line.split(" ")
  guess=l[0]
  correct=int(l[1][1:])
  res.append([map(int, list(guess)),correct])
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
    global restrictions, guesses, clues, big_inds
    for i, el in enumerate(s):
        if el >=0:
            if restrictions[i][el]:
                return

    if depth == len(g):
        print "".join(map(str,s))
        return

    #iterate over all combinations of clues for g
    nclues = clues[depth]
    guess = guesses[depth]
    if not nclues:
        for i, el in enumerate(guess):
            restrictions[i][el] += 1
        row_sol(s,g,depth+1)
        for i, el in enumerate(guess):
            restrictions[i][el] -= 1

    # for i, el in enumerate(s):
    #     if el < 0:
    #         if not restrictions[i,guess[i]]: inds.append(i)
    #     elif el == guess[i]:
    #         nclues -= 1
    #         oinds.append(i)

    inds = big_inds[np.logical_and(s < 0, restrictions[big_inds, guess] == 0)]
    oinds = big_inds[s == guess]
    nclues -= len(oinds)
    if nclues < 0:
        return
    # elif nclues == 0:
    #     for i, el in enumerate(guess):
    #         restrictions[i][el] += 1
    #     row_sol(s,g,depth+1)
    #     for i, el in enumerate(guess):
    #         restrictions[i][el] -= 1
    #     return

    for c in combinations(inds,nclues):
        if depth < 1:
            print depth*" " + str(c)

        cinds =  np.array(c, dtype = int)
        mask = np.ones(len(guess), dtype=int)
        mask[cinds] = 0
        mask[oinds] = 0
        rinds = big_inds[mask > 0]
        #rinds = []
        #for el in range(len(guess)):
        #    if el not in c and el not in oinds:
        #        rinds.append(el)
        #rinds = np.array(rinds)
        restrictions[rinds, guess[rinds]] += 1
        s[cinds] = guess[cinds]
        row_sol(s, g, depth+1)
        s[cinds] = -1
        restrictions[rinds, guess[rinds]] -= 1


res = parse_infile()
#print res
l=len(res[0][0])
#s=[-1]*l
s = -np.ones(l, dtype = int)
guesses = np.array([res[depth][0] for depth in range(len(res))])
clues = np.array([res[depth][1] for depth in range(len(res))], dtype = int)
#print s, guesses, clues
restrictions = np.zeros((l,10), dtype = int)
big_inds = np.arange(l, dtype=int)
row_sol(s,res,0)
