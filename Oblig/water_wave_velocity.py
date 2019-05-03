from math import pi,exp,tanh,sqrt
import numpy as np
import matplotlib.pyplot as plt

def wave(l):
        g=9.81
        s=7.9e-2
        d=1000
        h=50
        return np.sqrt((g*l)/(2*pi)*
                        (1+s*(4*np.pi**2)/(d*g*l**2))*
                        np.tanh ((2*np.pi*h)/l))
        
l=np.linspace(0.001,0.1,100)
m=wave(l)
plt.plot(l,m)
plt.show()

l=np.linspace(1,2000,4000)
m=wave(l)
plt.plot(l,m)
plt.show()
      






     
