from math import exp,pi,sin
from numpy import*
import matplotlib.pyplot as plt

def f(x,t):
        return exp(-(x-3*t)**2)*sin(3*pi*(x-t))

x=linspace(-4,4,41)
y=f(x,0)

plt.plot(x,y)
plt.show()



     
