from proj_euler import sphere_points

n = 10**10
s = 0
for p in sphere_points(n):
  s += abs(p[0])+abs(p[1])+abs(p[2])
print s
