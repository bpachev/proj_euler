from math import floor,log,ceil

def fibbo(n):
 if not n:
  return 0
 f0,f1 =0,1 
 for i in xrange(n):
  f0,f1 = f1,f0+f1
 return f0

def seq(x,prefix=False,pow2=None):
 s = [x]
 while not x == 1:
   if prefix:
    if x in pow2:
     return s
   if x%2:
    x = 3*x+1
   else:
    x = x/2
   s.append(x)
 return s

def num_sols(x,k):
 '''
 Collatx prefixes with k steps ending at x
 '''
 if not k:
   return 1
 if x % 6 == 4:
   return num_sols((x-1)/3,k-1) + num_sols(2*x,k-1)
 else:
   return num_sols(2*x,k-1)


def gen_flips(bound,n,pow2):
 flips = [] 
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
#       print "FLIP at %d on %d" % (i,x)
#       print seq(i)
       flips.append((i,l))
 return flips 

def solve(n):
 base = fibbo(n) #Prefix classes (defined by distinct up-down sequences)
 min_upsteps = ceil(n*log(3)/log(6))
 max_seq_0 = ((3./2)**(n-min_upsteps)-1.)/(3./2 - 1)
 flip_bound = int(floor(2.**min_upsteps/(2.**min_upsteps-3**(n-min_upsteps)) * max_seq_0))
 print "FLIP BOUND %d" % flip_bound
 
 pow2 = set([2**i for i in xrange(int(floor(log(flip_bound)/log(2)))+10)])
   
 #Now, analyze these flips
 flips = gen_flips(flip_bound,n,pow2)  
 
 print "TOTAL %d FLIPS" % len(flips)
 print flips
 return base
#the period of num_sols(n,k) appears to be 2*3**(k/2)
print solve(20)
