from math import*
import numpy as np
from matplotlib.pyplot import*

def h(x):
	return 1/sqrt(2*pi)*exp (-0.5*x**2) 
l=[]
x_values=np.linspace(-4,4,41)
for i in x_values:
     h_values=h(i)
     l.append(h_values)
     
b=np.array(l)
plot(x_values ,b)
show()

     
