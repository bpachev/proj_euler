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
tDict["CH3"] = {"GO":p,"JAIL":p,"C1":p,"E3":p,"R1":p,"H2":p,"R1":2*p,"U1":p,"CC3":p}

C
def 
