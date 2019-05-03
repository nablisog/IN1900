import numpy as np
import matplotlib.pyplot as plt
def exact(f):
     c=(f-32)*(5/9)
     return c

def simple(f):
     c=(f-30)/2
     return c


x=np.linspace(-20,120,200)
plt.plot(x,exact(x))
plt.plot(x, simple(x))
plt.show()












