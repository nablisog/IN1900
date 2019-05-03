from math import sin,exp,pi
import numpy as np
import matplotlib.pyplot as plt

def f(t):
	if 0 < t < T/2:
                return 1
	elif t ==T/2:
                return 0              
	elif T/2 < t < T:
                return -1
        

def S(t,n):
    
    s = 0
    for i in range(1, n+1):
        s += (1./(2*i-1)*np.sin(2*(2*i-1)*pi*t/T))
    s *= 4/pi
    return s
T = 2*pi
t = np.linspace(0, T, 701)
t = t[1:-1]  

f_exact = np.zeros(len(t))
for i in range(len(t)):
    f_exact[i] = f(t[i])


plt.plot(t, S(t, 1),
         t, S(t, 3),
         t, S(t, 20),
         t, S(t, 200),
         t, f_exact)

plt.show()


