import numpy as np
from scipy import linalg as la

squares = ["GO","A1","CC1","A2","T1","R1","B1","CH1","B2","B3","JAIL","C1","U1","C2","C3","R2","D1","CC2","D2","D3","FP","E1","CH2","E2","E3","R3","F1","F2","U2","F3","G2J","G1","G2","CC3","G3","R4","CH3","H1","T2","H2"]

rDict = {}
for i,sq in enumerate(squares):
  rDict[sq] = i

p = 1./16
tDict = {}
tDict["G2J"] = {"JAIL":1.}
tDict["CC1"] = {"GO":p,"JAIL":p}
tDict["CC2"] = {"GO":p,"JAIL":p}
tDict["CC3"] = {"GO":p,"JAIL":p}

tDict["CH1"] = {"GO":p,"JAIL":p,"C1":p,"E3":p,"R1":p,"H2":p,"R2":2*p,"U1":p,"T1":p}
tDict["CH2"] = {"GO":p,"JAIL":p,"C1":p,"E3":p,"R1":p,"H2":p,"R3":2*p,"U2":p,"D3":p}
tDict["CH3"] = {"GO":p,"JAIL":p,"C1":p,"E3":p,"H2":p,"R1":3*p,"U1":p,"CC3":p}

nSquares = len(squares)

#Prob is the probabiliity of entering the current state
def trans(start,prob=1.,curr_row = None,doubles=0,dice=6):
  global nSquares,squares,rDict,tDict
  if curr_row is None:
    curr_row = np.zeros(nSquares)
  for d1 in xrange(1,dice+1):
    for d2 in xrange(1,dice+1):
      isDouble = 1 if d1==d2 else 0
      if doubles + isDouble == 3:
        curr_row[rDict["JAIL"]] += prob/(dice**2)
        continue #go IMMEDIATELY to JAIL
      nPos = (start+d1+d2)%nSquares
      if squares[nPos] in tDict:
        rp = 1.
        td = tDict[squares[nPos]]
        for t in td:
          rp -= td[t] #probability that we stay on the square
          pLand = td[t]/dice**2 #probability of this transition happening
          if t == "CC3":
            curr_row[rDict["GO"]] += pLand*tDict["CC3"]["GO"]
            curr_row[rDict["JAIL"]] += pLand*tDict["CC3"]["JAIL"]
            pLand *= (1. - tDict["CC3"]["GO"] - tDict["CC3"]["JAIL"])
                        
          if isDouble:
            trans(rDict[t],prob*pLand,curr_row,doubles+1,dice)
          else:
            curr_row[rDict[t]] += prob*pLand
        
        if isDouble:
           trans(nPos,prob*rp/dice**2, curr_row,doubles+1,dice)
        else:
           #done
           curr_row[nPos] += prob*rp/dice**2
      else:
        if isDouble:
           trans(nPos,prob/dice**2,curr_row,doubles+1,dice)
        else:
           curr_row[nPos] += prob/dice**2  
            
  return curr_row

T = np.zeros((nSquares,nSquares))
for i in xrange(nSquares):
  T[:,i] = trans(i,dice=6)      

          
evals,evecs = la.eig(T)

print np.argsort(evecs[:,0])
pvec = evecs[:,0]/np.sum(evecs[:,0])*100
pvec = pvec.astype(float)

for i,s in enumerate(squares):
  print s + " probability " + str(pvec[i]) + "%"


for i in xrange(evals.shape[0]):
  if np.allclose(evecs[:,i],T.dot(evecs[:,i])):
    pvec = evecs[:,i]/np.sum(evecs[:,i])*100
    pvec = pvec.astype(float)
    print np.argsort(pvec)
    for i,s in enumerate(squares):
      print s + " probability " + str(pvec[i]) + "%"
    break     
    
        
