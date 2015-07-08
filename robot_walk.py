import numpy as np

#the same as num_walks, with a restriction on the number of counter-clockwise steps
#exactly k*arc CC steps must be taken
def restricted_walks(steps,arc,k):
  #construct states
  sDict = {}
  for r in xrange(arc):
    for sNum in xrange((k+1)**arc):
      tl = [r]
      t = sNum
      for j in xrange(arc):
         tl.append(t%(k+1))
         t /= (k+1)
      sDict[tuple(tl)] = 0
  sDict[tuple([0 for j in xrange(arc+1)])] = 1
  #init sum
  s = 0
  for i in xrange(steps):
    nDict = {state:0 for state in sDict}
    for state in sDict:
      #counterclockwise step
      if state[state[0]+1] < k:
       mState = list(state)
       mState[0] = (mState[0] + 1) % arc
       mState[state[0]+1] += 1
       nDict[tuple(mState)] += sDict[state]
            
      
      #clockwise step
      mState = list(state)
      mState[0] = (mState[0] - 1) % arc
      nDict[tuple(mState)] += sDict[state]
    sDict = nDict
#  print sDict
  return sDict[tuple([0]+[k for j in xrange(arc)])]


#steps is the number of walks
#arc is the fraction of a circle each step is. 2 corresponds to a half-circle, 3 to a third, 5 to a fifth, etc.
def num_walks(steps,arc):
 s = 0
 d = (steps/arc + 1)
 print d/2
 for i in xrange(d/2):
   s += 2*restricted_walks(steps,arc,i)
 if d % 2:
   s += restricted_walks(steps,arc,d/2)
 return s
 
print num_walks(70,5)

