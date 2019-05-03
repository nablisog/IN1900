from numpy import*
from matplotlib.pyplot import*

def RungeKutta2(f, U0, T, n):
     t = zeros(n+1)
     u = zeros(n+1)  

     u[0] = U0
     t[0] = 0
     dt = T/float(n)

     for k in range(n):
          K1 = dt*f(u[k], t[k])
          K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)
          t[k+1] = t[k] + dt
          u[k+1] = u[k] + dt*f(u[k], t[k])
         

     return u, t
     
def f(u,t):
     return u

w = RungeKutta2(f,U0=1,T=5,n=15)
x = linspace(0, 5, 101)
y = exp(x)
plot(x, y)
plot(w)
show()
     
        
