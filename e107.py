import networkx as nx
import numpy as np

filename = "p107_network.txt"

fp = open(filename,"r")
mat = np.loadtxt(fp,delimiter=",",dtype=str)
fp.close()
total = 0
red = 0

G = nx.Graph()

for i in xrange(mat.shape[0]):
  for j in xrange(i):
    if mat[i,j] == '-':
      mat[i,j] = 0
    else:
     temp = int(mat[i,j])
     total += temp
     G.add_edge(i,j,weight=temp)


T = nx.minimum_spanning_tree(G)
for e in T.edges(data=True):
 red += e[2]["weight"]
 
print "Savings: " + str(total-red)
