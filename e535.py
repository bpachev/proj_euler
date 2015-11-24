from proj_euler import isqrt,lin_sum,square_sum


def sum_isqrt(a,b):
 """
 Returns the sum of the integer part of sqrt(i) for i in xrange(a,b)
 But this is O(log(b)) (for the isqrt computation)
 a and b are positive integers, b > a.
 """
 ia,ib = isqrt(a),isqrt(b)
 if ia==ib:
  return ia*(b-a)
 return ia*((ia+1)**2-a) + ib*(b-(ib)**2) + lin_sum(ib-1)-lin_sum(ia) + 2*(square_sum(ib-1)-square_sum(ia))


#range of stuff in the fractal sequence
class RNG:
 #level is the fractal depth, a is the start of the interval (included), b is excluded
 def __init__(self,a,b,start_list=[]):
  self.a = a
  self.b = b
  self.level = len(start_list)
  self.start_list = start_list
  self.end_list = [b]  
  off=self.b-self.a
  start = self.a
  prod_pow=[]
  self.chil = [off]
  self.end_list = []
  for st in self.start_list:
   prod_pow.append(sum_isqrt(start,start+off))
   off = sum(prod_pow)
   self.chil.append(off)
   self.end_list.append(off+st)
   start = st

  
 def sum_els(self):
  s = lin_sum(self.b-1)-lin_sum(self.a-1)
  for i,el in enumerate(self.start_list):
    s += lin_sum(el+self.chil[i+1]-1)-lin_sum(el-1)
  return s  
   
 def num_els(self):
   return sum(self.chil)
 
 def deepen(self,new_start):
  return RNG(self.a,self.b,self.start_list+[new_start])
   


def dumb(n):
 seq = [1,1]
 c1 = 2
 c2 = 1 #counter for 2-level sequence
 l=2
 while True:
  if l == n:
   print seq
   return sum(seq)
  next = seq[c2]
  nsteps = isqrt(next)
  for ind in xrange(nsteps):
   seq.append(c1+ind)
   if l+ind+1==n:
    print seq
    return sum(seq)
  c1 += nsteps
  seq.append(next)
  l = l+nsteps+1
  c2+=1

#print dumb(r.num_els()+r2.num_els())

#smarter 1
def sm1(n):
 r = RNG(1,2)
 r_last = RNG(1,2)
 while r.num_els()<n:
  r_last = r
  r = r.deepen(1)
 r = r_last
 nels = r.num_els()
 s = r.sum_els()
 while True:
  if nels==n:
   return s
  d = len(r.end_list)
  for i in xrange(d+1):
   if not i:
    nr = RNG(r.b,r.b+1,r.end_list[i:])
   elif i==d:
    s+=lin_sum(r.end_list[i-1]+n-nels-1) -lin_sum(r.end_list[i-1]-1)
    print s
    return s
   else:
    nr = RNG(r.end_list[i-1],r.end_list[i-1]+1,r.end_list[i:])
   if nels+nr.num_els() <= n:
    nels += nr.num_els()
    s += nr.sum_els()
    r = nr
    break
 print s
 return s

print sm1(10**18)%10**9
