from itertools import combinations

filename = "p105_sets.txt"

def is_special(a):
    l = len(a)
    
    #test property 2, that sums of disjoint subsets with more elements are greater than those with less
    for i in xrange(2,l):
      if sum(a[:i]) <= sum(a[1-i:]):
        return 0
    
    #test that sums of subsets cannot be equal
    for i in xrange(1,l/2+1):
      sums = set()
      for c in combinations(a,i):
        t = sum(c)
        if t in sums:
          return 0
        else:
          sums.add(t)
    return 1    

s = 0
with open(filename,'r') as f:
  for line in f:
    a = sorted(map(int,line.strip().split(",")))
    if is_special(a):
     s += sum(a)
     print str(a) + " is a special set"

print s

