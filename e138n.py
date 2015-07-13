from proj_euler import isqrt


n = 12
sols = []

x,y = 305,272

xr1 =  (-9,-10,-8)
yr1 =  (-8,-9,-8)
xr2 =  (-9,-10,8)
yr2 =  (-8,-9,8)

s = 0
sols = []
for i in xrange(n-1):
  sols.append(abs(x))
  print x,y
  print 4*x*x - 5*y*y-8*y -4
  if 1:
    x_new = xr1[0]*x +xr1[1]*y + xr1[2]
    y_new = yr1[0]*x+ yr1[1]*y + yr1[2]
    x = x_new
    y = y_new

x,y = 17,16

for i in xrange(n):
    print x,y,4*x*x - 5*y*y+8*y -4
    sols.append(abs(x))
    x_new = xr2[0]*x +xr2[1]*y + xr2[2]
    y_new = yr2[0]*x+ yr2[1]*y + yr2[2]
    x = x_new
    y = y_new
print sols
print (17+sum(sols))/2

