from itertools import product
import sys
sols = set()

if len(sys.argv) >= 2:
 CAP = int(sys.argv[1])
else:
 CAP = 3000
if len(sys.argv) >= 3:
 thresh = int(sys.argv[2])
else:
 thresh = 10**6 
s = 0
sq_list = [i*i for i in xrange(1,3*CAP+1)] 
sq_set = set(sq_list)
sols = {i:0 for i in xrange(1,CAP+1)}

#max_side
for i in xrange(CAP):
  #sum of min sides
  for j in xrange(2*CAP):
    ir = i+1
    jr = j+1
    if jr > 2*ir:
      break
    if sq_list[i] + sq_list[j] in sq_set:
      s += min(ir,jr-1) - ((jr+1)/2) + 1
      sols[i+1] += min(ir,jr-1) - ((jr+1)/2) + 1

print "Num Sols for CAP=" + str(CAP) + " is " + str(s)
cval = 0
for i in xrange(1,CAP+1):
  cval += sols[i]
  if cval > thresh:
    print "First M for which the number of solutions exceeds "+str(thresh)+" : " + str(i)
    break
