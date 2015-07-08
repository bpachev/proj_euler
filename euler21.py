import numpy as np

def amicable_sum(n):
  s = 0
  d_arr = np.zeros(n)
  def d(x):
    r = 1
    if x <= 1:
      return 0
    if x <= n:
      if d_arr[x-1]:
        return d_arr[x-1]
      else:
        sq = x**(.5)
        for i in xrange(2,int(sq)):
          if x % i == 0:
            r += i + x / i
        if sq == int(sq):
          r += sq
        d_arr[x-1] = r
        return r
        
    else:
      sq = x**(.5)
      for i in xrange(2,int(sq)):
        if x % i == 0:
#          print str(i) + " " + str(x/i) + " " + str(x) + " " + str(r)
          r += i + x / i
      if sq == int(sq):
        r += sq      
      return r
  
  for j in xrange(1,n):
    temp = d(j)
    if d(temp) == j and not temp == j:
      s += j
 #     print j
#  print d(28)
  return s
  
print amicable_sum(10000)