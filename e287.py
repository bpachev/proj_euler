
def isBlack(x,y,radius):
  return (x-radius)**2 + (y-radius)**2 <= radius**2

def qTree(x,y,sLen,r):
  if isBlack(x,y,r) and isBlack(x-sLen+1,y-sLen+1,r) and isBlack(x-sLen+1,y,r) and isBlack(x,y-sLen+1,r):
    return 2
  if not isBlack(x,y,r) and not isBlack(x-sLen+1,y-sLen+1,r) and not isBlack(x-sLen+1,y,r) and not isBlack(x,y-sLen+1,r):
    return 2
  
  return 1 +  qTree(x,y,sLen/2,r) + qTree(x-sLen/2,y,sLen/2,r) + qTree(x,y-sLen/2,sLen/2,r) + qTree(x-sLen/2,y-sLen/2,sLen/2,r)

cap = 2**24
print 1 + qTree(cap-1,cap-1,cap/2,cap/2) + qTree(cap/2-1,cap-1,cap/2,cap/2) + qTree(cap-1,cap/2-1,cap/2,cap/2) + qTree(cap/2-1,cap/2-1,cap/2,cap/2)

