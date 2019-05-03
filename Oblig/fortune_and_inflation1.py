from numpy import*
f=100
p=5
q=5
N=4
i=2
x0=f
c0=((p*q)/1e4)*f
l=range(N+1)
x = zeros(len(l))			
c = zeros(len(l))
x[0]=x0
c[0]=c0
for n in range(1,N):
     x[n]=x[n-1] + p/100 * x[n-1] - c[n-1]
     c[n]=c[n-1] + i/100 * c[n-1]
     

import matplotlib.pyplot as p
p.plot(l,x)
p.show()
#values for p and N, i just used from growth_years_efficient.py and for others
# i just asigned them myself

     
     
