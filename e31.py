import itertools
import numpy as np

num_combos = 1 #for the cases where one 200p, coin is included


for x in itertools.product(range(3),range(5),range(11),range(21),range(51),range(101)):
  if 100*x[0] + 50*x[1] + 20*x[2] + 10*x[3] + 5*x[4] + 2*x[5] <= 200:
  num_combos += 1
    
    
print "The number of ways to make two pounds is: " + str(num_combos)