from scipy.misc import comb

def p(n):
 tot = 0
 #first character
 for p1 in xrange(1,26+1):
  #second character
  for p2 in xrange(p1+1,26+1):
   middle = p2-p1-1 #number of chars lexicographically between p1 and p2
   #number of characters before p1 p2 in the string
   for before in xrange(n-1):
    after = n-2-before
    if after > p2-2:
     continue         
    for bm in xrange(max(before+p2-26,0),middle+1):
     for am in xrange(min(middle-bm+1,after+1)):
      t = comb(middle,bm,True)*comb(middle-bm,am,True)*comb(26-p2,before-bm,True)*comb(p1-1,after-am,True) 
      tot += t
 return tot
print max([p(n) for n in xrange(3,27)])
