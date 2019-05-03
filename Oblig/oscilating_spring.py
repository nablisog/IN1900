from math import cos,exp,sqrt,pi
import numpy as np

k=4
sign=0.15
m=9
a=0.3
lis_t=range(0,26)
lis_y=[]
for i in lis_t:
     z=a*exp(-sign*i)*cos(sqrt((k/m)*i))
     lis_y.append(z)

t_array=np.array(lis_t)
y_array=np.array(lis_y)

import matplotlib.pyplot as plt
plt.plot(t_array,y_array)
plt.show()

def osci(t):
     k=4
     sign=0.15
     m=9
     a=0.3
     return a*exp(-sign*t)*cos(sqrt((k/m)*t))
x=np.linspace(0,25,101)
vector=np.vectorize(osci)
vectorizer=vector(x)
plt.plot(x,vectorizer)
plt.show()






     
     
     
