from itertools import combinations,permutations

squares = set()
for i in xrange(1,int(10**4.5)):
  squares.add(i*i)

def seq_to_num(s):
 t = 0
 for i in s:
  t *= 10
  t += i
 return t 

def sq_anag(d):
  global squares
  md = {}
  for k in combinations(range(10),d):
    for p in permutations(list(k)):
       if p[0] == 0:
         continue
       t = seq_to_num(p)
       if t in squares:
        if not k in md:
         md[k] = [t]
        else:
         md[k].append(t)
#  print md
  return md

def apply_permu(pdict,l):
  nl = []
  for i in xrange(len(l)):
    nl.append(l[pdict[i]])
  return nl  

permu_dicts = {}
for i in xrange(2,10):
  permu_dicts[i] = sq_anag(i)

m = 0 #max
with open("p098_words.txt") as f:
  for line in f:
    words = line.strip('"').split('","')
    
sorted_words = [''.join(sorted(w)) for w in words]
w_dict = [{w[i]:i for i in xrange(len(w))} for w in words]
for i in xrange(len(words)):
  for j in xrange(i,len(words)):
    if not i == j and sorted_words[i] == sorted_words[j]:
      print words[i] + " is an anagram of " + words[j]
      clen = len(words[j])
      pDict = {k:w_dict[i][words[j][k]] for k in xrange(clen)}
      #if not clen == 3:
       # continue
      #print pDict
      for p in permu_dicts[clen]:
        #print p
        for sq in permu_dicts[clen][p]:
          temp = seq_to_num(apply_permu(pDict,map(int,list(str(sq)))))
          #print sq
          #print temp
          if temp in permu_dicts[clen][p]:
            print str(temp) +" and " + str(sq)
            if temp > m:
              m = temp
            if sq > m:
              m = sq
print m



