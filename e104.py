import proj_euler as pe

ph,pl = 1,1
ch,cl = 1,1
nh,nl = 2,2
p = "123456789"
for i in xrange(1000000):
  ph,pl = ch,cl
  ch,cl = nh,nl
  nl = (cl + pl) % 10**9
  nh = ph + ch
  if nh >= 10**20:
    nh /= 10
    ch /= 10
    ph /= 10
  if len(str(nh)) >= 9:
    if pe.permu(p,str(nh)[0:9]) and pe.permu(p,str(nl)[-9:]):
      print "F("+str(i+4)+")'s first and last nine digits are pandigital"
 #   if pe.permu(p,str(nh)[0:9]):
  #    print "F("+str(i+4)+")'s first nine digits are pandigital"
 
   # if pe.permu(p,str(nl)[-9:]):
    #  print "F("+str(i+4)+")'s last nine digits are pandigital"

