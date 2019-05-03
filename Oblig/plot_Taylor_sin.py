from math import factorial
from numpy import*
import matplotlib.pyplot as p
def S(x, n):
	s=0
	for j in range(n+1):
	  s = s + (-1)** j* x**(2*j+1)/ factorial(2*j+1)
	return s      
x=linspace(0,4*pi,101)
p.plot(x,sin(x))

for n in [1,2,3,6,12]:

        
 p.plot(x,S(x,n))
 
p.ylim([-1, 2])
p.show()


