import itertools

for inner in itertools.combinations(range(1,10),5):
  s = sum(inner)
  if s % 5:
    continue
  k = 11 + s / 5
  for ordered_inner in itertools.permutations(list(inner)):
    digit_mask = {d:1 for d in range(1,11)}
    for i in inner:
      digit_mask[i] = 0
    digit_mask[10] = 0
    os = []
    if not ordered_inner[0] + ordered_inner[1] + 10 == k:
      continue
    success = True
    for j in xrange(1,5):
      if j == 4:
        o = o = k - ordered_inner[j] - ordered_inner[0]
      else:
        o = k - ordered_inner[j] - ordered_inner[j+1]
      if o > 9 or o < 1:
        success = False
        break

      if not digit_mask[o]:
        #already used. FAIL.
        success = False
        break
      digit_mask[o] = 0
      os.append(o)
    if not success:
      continue
    print ordered_inner
    print k
    print os
