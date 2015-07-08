def num_divs(n):
  divs = 0 
  for x in xrange(1,int(n**0.5)):
    if n % x == 0:
      divs += 2
  if int(n**0.5) == n**0.5:
   divs += 1
  return divs
      
def find_first_triag(m):
  e = 0
  while True:
    e += 1
    n = e*(e+1)/2
    d = num_divs(n)
    if d >= m:
      return n

print find_first_triag(500)