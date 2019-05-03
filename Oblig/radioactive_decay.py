from numpy import*
from matplotlib.pylab import*
class Decay:
     def __init__(self, a):
          self.a = a

     def __call__(self, u):
          a = self.a
          return -a*u

#function forwardEuler is taken from lecture 
def ForwardEuler(f, U0, T, n):
     t = zeros(n+1)
     u = zeros(n+1)
     u[0] = U0
     t[0] = 0
     dt = T/float(n)
     for k in range(n):
          t[k+1] = t[k] + dt
          u[k+1] = u[k] + dt*f(u[k], t[k])

     return u,t

def f(u,t):
     return -a*u

def f_1(t):
     return exp(-a*t)

a = log(2)/5600
d = Decay(a) 
U0 = 1
T = 20000
dt = 500
n = T/dt
x, y = ForwardEuler(f, U0, T, n)
plot(x, y)
plot(f_1(t), t)
show()

    
          
