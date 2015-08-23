from math import floor,log,ceil

from itertools import combinations
cache = {}
mcache = 20
mods = [1] + [2*3**(n-n/2) for n in xrange(1,mcache+1)]
def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)

def fibbo(n):
 if not n:
  return 0
 f0,f1 =0,1 
 for i in xrange(n):
  f0,f1 = f1,f0+f1
 return f0

def seq(x,prefix=False,pow2=None,verbose=False):
 s = [x]
 while not x == 1:
   if x%2:
    x = 3*x+1
   else:
    x = x/2
   if prefix:
    if x in pow2:
     return s
   if verbose:
    print x
   else:
    s.append(x)
 return s

def num_sols(x,k):
 '''
 Collatx prefixes with k steps ending at x
 '''
 global mods,cache,mcache
 if k <0:
  print k,x,seq(x),len(seq(x))
 if not k:
   return 1
 if k <= mcache:
   if (x%mods[k],k) in cache:
    return cache[(x%mods[k],k)]
 if x % 6 == 4:
   if k <= mcache:
    t = num_sols((x-1)/3,k-1) + num_sols(2*x,k-1)
    cache[(x%mods[k],k)] = t
    return t
   return num_sols((x-1)/3,k-1) + num_sols(2*x,k-1)
 else:
  if k <= mcache:
    t = num_sols(2*x,k-1)
    cache[(x%mods[k],k)] = t
    return t
  return num_sols(2*x,k-1)

def f_inv(n):
 return 2*n
def g_inv(n):
 return (x-1)/3

def shared_prefixes(l,k,flip_set):
 need_g = 1
 saw_flip = 0
 if not k:
   return 1
 for x in l:
   if x in flip_set:
    saw_flip = 1
    break
   if not x % 6 == 4:
     need_g = 0
     break
 
 if saw_flip:
   not_all_flip = 0
   for x in l:
    if x not in flip_set:
      not_all_flip = 1
      break
   if not_all_flip:
     return 0
   else:
    print "FOUND a case where all were flips"
    tpow2 = set([2**i for i in xrange(64)])
    first_pref = argsort(seq(x,True,tpow2))
    not_all_match = 0
    for x in l:
      if not argsort(seq(x),True,tpow2) == first_pref:
        not_all_match = 1
        break
    if not_all_match:
      print "FOUND a case where all were flips and did not match"
      return 0
    print "FOUND a case where all were flips and matched"
 
 if need_g:
  return shared_prefixes(map(f_inv,l),k-1,flip_set) + shared_prefixes(map(g_inv,l),k-1,flip_set)
 return shared_prefixes(map(f_inv,l),k-1,flip_set)    
 
def next_collatz(x):
 if x%2:
  return 3*x+1
 else:
  return x/2

def gen_flips(bound,n,pow2):
 flips = []
 flip_set = set() 
 for i in xrange(3,bound+1):
   x = i
   l = 1
   a,b = 1.,0. #x = a*start + b The coefficients will depend on the up-down steps
   while x not in pow2 and l <= n:
     l += 1
     if x % 2:
       x = 3*x + 1
       a ,b = 3*a, 3*b + 1
     else:
       x,a,b = x/2,a/2,b/2
     # our start was on the finite side of the interesting point
     if i <= -b/(a-1.):
       if x in pow2:
         break #not really part of the prefix
       if l==n:         
         x_next = next_collatz(x)
         if x_next not in pow2:
           break #prefix longer than n
       if len(seq(i,True,pow2)) > n:
        break
       flip_set.add(i)
 return flip_set 

def bound(n):
 min_upsteps = ceil(n*log(3)/log(6))
 max_seq_0 = ((3./2)**(n-min_upsteps)-1.)/(3./2 - 1)
 return int(floor(2.**min_upsteps/(2.**min_upsteps-3**(n-min_upsteps)) * max_seq_0))
 

def solve(n):
 #Must substract one because the sequence of all downs is trivial
 base = fibbo(n) #Prefix classes (defined by distinct up-down sequences)
 flip_bound = max([bound(i) for i in xrange(1,n+1)])
 print "FLIP BOUND %d" % flip_bound
 
 pow2 = set([2**i for i in xrange(int(floor(log(flip_bound)/log(2)))+100)])
   
 flip_set = gen_flips(flip_bound,n,pow2)
 print "Generated Flips"
 #Now, analyze these flips
 prefix_hash = {} #maps prefix family to flips
 for flip in flip_set:
   fseq = seq(flip,True,pow2)
   if len(set(fseq).intersection(flip_set)) > 1:
     #Another flip start is in the sequence of flip, so it can be excluded from counting.
     continue
   ind = tuple(argsort(fseq))
   print num_sols(flip,n-len(ind))
   base += num_sols(flip,n-len(ind))
   if ind in prefix_hash:
    prefix_hash[ind].append(flip)
   else:
    prefix_hash[ind] = [flip]
 print prefix_hash.values()
 print "TOTAL %d FLIPS" % len(flip_set)
 print flip_set
 for prefix in prefix_hash:
  l = len(prefix_hash[prefix])
  pl = len(prefix)
  if l > 1:
    for i in xrange(2,l+1):
      for c in combinations(prefix_hash[prefix],i):
        base += (-1)**(l-1) * shared_prefixes(c,pl)
 return base
#the period of num_sols(n,k) appears to be 2*3**(k-k/2)
print solve(90)
