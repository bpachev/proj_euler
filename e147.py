def rects(h,w):
  return ((h+1)*h*w*(w+1))/4

def layer_ends(y,short,middle):
  if y < short:
    return -y, y+1
  elif y >= short and y < short + middle:
    return   y + 1 - 2*short, y+1
  else:
    return  y + 1 - 2*short, 2*(short+middle) - y    

def count_corner1(h,w,short_layers,middle_layers):
  s = 0
  l_len = 2 #layer length
  # count recs originating in first corner
  for i in xrange(short_layers):
    for j in xrange(l_len):
      n_mid_lays = j+1 #number of middle layers that WOULD be punctured given infinite such layers
      if n_mid_lays <= middle_layers:
        s += (short_layers - i + n_mid_lays) * (l_len - j)
      else:
        s +=  (short_layers - i + middle_layers) * (l_len - j)
        #Now count rectangles that end in the opposite corner
        s += corner_2_point(short_layers,middle_layers,i,j-i)
        
    l_len += 2
  return s

def corner_2_point(short_layers,middle_layers,x,y):
  s = 0
  starty = max(short_layers + middle_layers,y)
  for yl in xrange(starty,2*short_layers+middle_layers):
    startx, endx = layer_ends(yl,short_layers,middle_layers)
    s += max(0, 1 + endx-x)
  return s

#Counts ONLY the side ones
def cross_hatched(h,w):
  if h > w:
    w,h = h,w
  if h == 1:
    return w-1
  s = 0
  short = h-1 #one corner
  middle = w-h
  
  for y in xrange(0,2*short+middle):
    st,endt = layer_ends(y,short,middle)
#    print st,endt,y
    for x in xrange(st,endt+1):
      for y_next in xrange(y,2*short+middle):
        st,end = layer_ends(y_next,short,middle)
        if x < st:
          break
        end = min(end,endt)
        s += max(0,1+end-x)
  return s
w,h = 47,43
s = 0
for i in xrange(1,h+1):
  for j in xrange(1,w+1):
    s += cross_hatched(i,j)+rects(i,j)
#    print i,j,cross_hatched(i,j)+rects(i,j) 

print s

