from proj_euler import sphere_points
import numpy as np
import networkx as nx
from math import acos
from itertools import product

def sphere_dist(p1,p2,r):
  return acos(np.dot(np.array(p1),np.array(p2))/float(r*r))/np.pi

def path_len_old(r):
  G = nx.Graph()
  points = sorted(list(sphere_points(r)))
#  print len(points)
  for i,p1 in enumerate(points):
    for j,p2 in enumerate(points):
      if not i == j:
        G.add_edge(p1,p2,weight=sphere_dist(p1,p2,r)**2)
#  print nx.shortest_path(G,(r,0,0),(-r,0,0),weight="weight")        
  return nx.shortest_path_length(G,(r,0,0),(-r,0,0),weight="weight")

def path_len(r):
  G = nx.Graph()
  points = sorted(list(sphere_points(r)))
  print len(points)
  bands = [[]]
  curr_band = -r
  for p1 in points:
    if p1[0] == curr_band:
      bands[-1].append(p1)
    else:
     curr_band = p1[0]
     bands.append([p1])
  
  l = len(bands)
  look_ahead=4
  tol = 1./(l-1)
  for i in xrange(l-1):
    for j in xrange(look_ahead):
      if i==l-1-j:
        break
      for p1,p2 in product(bands[i],bands[i+1+j]):
        d = sphere_dist(p1,p2,r)**2
        if d < tol or j==1:
          G.add_edge(p1,p2,weight=d)
  print len(G.edges())  
#  print [b[0][0] for b in bands]
#  for i,p1 in enumerate(points):
#    for j,p2 in enumerate(points):
#      if not i == j:
#        G.add_edge(p1,p2,weight=sphere_dist(p1,p2,r)**2)
#  print nx.shortest_path(G,(r,0,0),(-r,0,0),weight="weight")        
  return nx.shortest_path_length(G,(r,0,0),(-r,0,0),weight="weight")

s = 0
for i in xrange(1,16):
  print "On " + str(i)
  s += path_len(2**i-1)
#  print ,path_len_old(2**i-1)
print s

