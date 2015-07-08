import math

def expected_sheets(a2,a3,a4,a5):
  if a2 < 0 or a3 < 0 or a4 < 0 or a5 < 0:
    return 0.
  if not a2 and not a3 and not a4 and a5==1:
    return 0.
  
  
  elif not a2 and not a3 and  a4==1 and not a5:
    return 1. + expected_sheets(0,0,0,1)
  elif not a2 and a3==1 and not a4 and not a5:
    return 1. + expected_sheets(0,0,1,1)
  elif a2==1 and not a3 and not a4 and not a5:
    return 1. + expected_sheets(0,1,1,1)
  
  s = a2+a3+a4+a5
  return (float(a2)/s)*expected_sheets(a2-1,a3+1,a4+1,a5+1) + (float(a3)/s)*expected_sheets(a2,a3-1,a4+1,a5+1) + (float(a4)/s)*expected_sheets(a2,a3,a4-1,a5+1) + (float(a5)/s)*expected_sheets(a2,a3,a4,a5-1)
print expected_sheets(1,1,1,1)

