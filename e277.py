#Finds the smallest integer > cap with the given collatz prefix. seq is a string representation of the prefix
seq = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
#seq = "DdDddUUdDD"
denom = 1
coeff = 1
C = 0
for f in seq:
  if f == "U":
    C *= 4
    coeff *= 4
    C += 2*denom
    
  if f == "d":
    C *= 2
    coeff *= 2
    C -= 1*denom

  denom *= 3

cap = 10**15+1
rem = (-C*pow(coeff,2*denom/3-1,denom)) % denom

print cap + (rem-cap)%denom
