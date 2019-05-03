from math import*
import numpy as np
from matplotlib.pyplot import*

def h(x):
	return 1/sqrt(2*pi)*exp (-0.5*x**2)

x=np.linspace(-4,4,41)
a=np.vectorize(h)
b=a(x)
plot(x,b)
show()

