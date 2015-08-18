import networkx as nx
import numpy as np
from itertools import combinations

def savings(r1,r2):
  '''
  The savings in length when two spheres of radius r1 and r2 are placed in a pipe of radius 100.
  It is assumed that 25 < r1,r2 <= 50 
  '''
  T = r1+r2
  return T - (T*T-(100-T)**2)**.5

def open_tour(d):
  '''
  A variant of Traveling Salesman where the path need not end at the start.
  d is the distance matrix
  We only care about the minimum cost.
  '''
  N = d.shape[0]
  bit_mask = [2**i for i in xrange(N)]
  cache = np.zeros((2**N,N))
  for i in xrange(N):
    for j in xrange(i+1,N):
      cache[bit_mask[i]+bit_mask[j],i] = d[j,i]
      cache[bit_mask[i]+bit_mask[j],j] = d[i,j]
  
  r = range(N)
  for s in xrange(3,N+1):
    for c in combinations(r,s):
      mask = 0
      for e in c:
       mask += bit_mask[e]
      
      for e in c:
       m = 10
       for f in c:
         if f==e:
          continue
         m = min(m,cache[mask-bit_mask[e],f]+d[f,e])
       cache[mask,e] = m
#  print cache,d
  row = cache[-1,:]
  ma = 2**N-1
  for i in xrange(N-1):
   n = np.argmin(row)
   print n,bin(ma)      
   ma -= bit_mask[n]
   row = d[n,:]+cache[ma,:]
   
  return np.min(cache[-1,:])



N = 50
total = (N*(N+1)-29*30)
edges = {x:[] for x in xrange(30,N+1)}
edge_list = []
d = np.zeros((N-29,N-29))
for i in xrange(30,N):
 for j in xrange(i+1,N+1):
   edge_list.append((savings(i,j),i,j))
   d[i-30,j-30] = -1*savings(i,j)
   d[j-30,i-30] = d[i-30,j-30]
print (total+open_tour(d))*1000
G = nx.Graph()
def add_edge(i):
  global edge_list,edges,g
  l = edge_list.pop(i)
  G.add_edge(l[1],l[2])
  if len(nx.cycle_basis(G)):
    G.remove_edge(l[1],l[2])
    add_edge(0)
    return
  edges[l[1]].append(l[2])
  edges[l[2]].append(l[1])
  if len(edges[l[1]]) == 2:
    purge(l[1])
  if len(edges[l[2]]) == 2:
    purge(l[2])
  return
def purge(i):
  global edge_list
  for j,e in enumerate(edge_list):
    if e[1] == i or e[2]==i:
      del edge_list[j]
dec=0      
edge_list = sorted(edge_list)[::-1]
#print edge_list
#only need 20 edges maximum
for i in xrange(N-30):
  dec+= edge_list[0][0]
  add_edge(0)
print dec
print edge_list[0]
print edges,G.edges()
print 1000*total

