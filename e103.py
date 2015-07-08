def gen_special_sets(n,cap):
  minVal = n*cap
  minSet = []
  setSums = {}
  sets = set()
  ls = []
  for i in xrange(1,cap):
   for j in xrange(i+1,cap):
    for k in xrange(j+1,min(i+j+1,cap)):
     sets.add((i,j,k))
     ls.append([i,j,k])
     setSums[(i,j,k)] = set([i,j,k,i+j,i+k,j+k,i+j+k])
  for i in xrange(4, n+1):
    newLs = []
    newSets = set()
    newSetSums = {}
    for l in ls:      
      if len(l) >= i:
       continue
      strictMinVal = sum(l[(i-1)-(i-1)/2:]) - sum(l[0:(i-1)/2])
      for j in xrange(strictMinVal+1,l[0]):
        if j in l:
          continue
        flag = 1
        for k in xrange(i-1):
          temp = [el for el in l]
          temp.remove(l[k])
          temp.append(j)
          if not tuple(sorted(temp)) in sets:
            flag = 0
            break
        
        ss = setSums[tuple(l)]
        for subsetSum in ss:
          if j+subsetSum in ss:
            flag = 0
            break
            
        if flag:
          t = sorted(l + [j])
          tt = tuple(t) 
          newLs.append(t)
          newSets.add(tt)
          setSums[tt] = set()
          for subsetSum in ss:
            setSums[tt].add(j+subsetSum)
            setSums[tt].add(subsetSum)
          s = sum(t)
          if i == n and s < minVal:
            minVal = s
            minSet = t
          
    sets = newSets
    ls = newLs
  print minVal
  print minSet
  return newSets 
      

print len(gen_special_sets(7,50))
  
