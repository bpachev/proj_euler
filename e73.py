denom = 12000
s = 0

a,b = 0,1
c,d = 1,denom

while True:
  if c == 1 and d == 2:
    break
  if 3*c > d:
    s += 1
  t1,t2 = c,d
  c,d = (denom + b)/d*c - a, ((denom + b)/d)*d - b
  a,b = t1,t2
  
print s 
  
