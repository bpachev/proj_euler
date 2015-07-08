from proj_euler import MillerRabin

cap = 150000000
s = 0
for i in xrange(10,cap,2):
  if i % 1000000 == 0:
    print "On " + str(i)  + " Sum " + str(s)
  if not i%3 or not i%7 or not i%13:
    continue
  sq = i*i
  if MillerRabin(sq+1) and MillerRabin(sq+3) and MillerRabin(sq+7) and MillerRabin(sq+9):
    if MillerRabin(sq+13) and MillerRabin(sq+27):
      f = 1
      for j in xrange(15,27,2):
        if MillerRabin(sq+j):
          f = 0
          break
      if f:
        s += i
print s
