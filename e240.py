fact = [1]
for i in xrange(1,21):
 fact.append(i*fact[-1])

def count_dice(base,path):
 global fact
# print path
 mul = fact[base+len(path)]
 s = 0
 last = path[-1]
 curr = path[0]
 c = 0
 for d in path:
   if not d == curr:
    mul /= fact[c]
    c = 1
    curr = d
   else:
    c += 1
# print c
 for nl in xrange(c,c+base+1):
  s += (mul/fact[nl]/fact[base-(nl-c)]) * (last-1)**(c+base-nl)
 return s

def top_dice(base,top,s,path):
 t = 0
 if s == 0:
  if top:
   return 0
  else:
   return count_dice(base,path[1:])
 if not top and s:
   return 0
 
 for i in xrange(s/top,min(path[-1],s)+1):
  t += top_dice(base,top-1,s-i,path+[i])
 return t

t = 10
n = 20
s = 70
d = 12

print top_dice(n-t,t,s,[d])
