def spiral_sum(n):
  inc = 2
  s = 0
  num = 1
  for x in xrange(4*n + 1):
    s += num
    num += inc
    if x % 4 == 3:
      inc += 2
      
  return s

print spiral_sum(500)