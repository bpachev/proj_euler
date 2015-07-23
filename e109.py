from itertools import product
max_score = 100
dart_vals = {}

for i in xrange(1,21):
 t = str(i)
 dart_vals["S"+t] = i
 dart_vals["D"+t] = 2*i
 dart_vals["T"+t] = 3*i

dart_vals["D25"] = 50
dart_vals["S25"] = 25

scores = dart_vals.keys()
ranks = {k:i for i,k in enumerate(scores)}
#print ranks
s = 0
for i in xrange(1,4):
  for c in product(scores,repeat=i):
    if i ==3:
      if ranks[c[0]] < ranks[c[1]]:
        continue
    if not c[i-1][0] == "D":
      continue
    
    turn_score = 0
    for dart in c:
      turn_score += dart_vals[dart]
    
    if turn_score >= max_score:
      continue
    else:
      s += 1
print s
    
