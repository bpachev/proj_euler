infile="number_mind_test.txt"

gs = []
with open(infile,"r") as f:
 for line in f:
   line = line.strip().split(" ")
   gs.append([line[0],line[1][1]])



