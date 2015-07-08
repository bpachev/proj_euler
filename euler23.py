import numpy as np

def d(x):
  r = 1
  if x <= 1:
    return 0
  else:
    sq = x**(.5)
    if int(sq) == 1:
      return 1;
    for i in xrange(2,int(sq)):
      if x % i == 0:
        r += i + x / i
    if sq == int(sq):
      r += sq
    elif x % int(sq) == 0:
      r += int(sq) + x / int(sq)
    return r


def find_nonabundant_sums(cap,num_abundant):
  ab_nums = np.zeros(num_abundant)
  curr_ind = 0
  mask = np.arange(cap)
#  print mask[345];
  s = 0
#  print d(12)
  for x in xrange(cap):
    divs = d(x)
    if x < divs:
      ab_nums[curr_ind] = x
      curr_ind += 1
      for j in xrange(curr_ind):
        s = x + ab_nums[j]
        if s < cap:
 #         print ab_nums
          mask[s] = 0
  print np.sum(mask)
  print curr_ind
#  print mask[(mask > 0)]
  
      
#foo = np.arange(25)
#print np.sum(foo) - 24
print d(900)    
find_nonabundant_sums(2000,10000)