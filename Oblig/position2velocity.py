
with open("pos.txt","r") as infile:
     s = float(infile.readline())
     a=[]
     b=[]
     for lines in infile:
          words = lines.split()
          a.append(float(words[0])) 
          b.append(float(words[1]))

import numpy as np
x=np.array(a)
y=np.array(b)

import matplotlib.pyplot as p
p.plot(x,y)
p.show()

velo_x=[]
velo_y=[]
time=[]

for k in range(len(x)-1):
     v_x=(x*[k+1]-x*[k])/s
     v_y=(y*[k+1]-y*[k])/s
     t=k*s        
     velo_x.append(v_x)
     velo_y.append(v_y)
     time.append(t)
     
import numpy as np
x1=np.array(velo_x)
y1=np.array(velo_y)
t1=np.array(time)

import matplotlib.pyplot as p
p.plot(t1,x1)
p.plot(t1,y1)
p.show()









     


