from numpy import*
import matplotlib.pyplot as plt


b1 = 0.0005
b2 = 0.0001
v = 0.1
dt = 0.5
t = 60
n = int(t/dt)
time = linspace(0, t, n+1)


for betta in [b2, b1]:
      
     S = zeros(n+1)
     I = zeros(n+1)
     R = zeros(n+1)
     
     S[0]=1500
     I[0]=1
     R[0]=0
     
     
     for i in range(n):
          S[i+1] = S[i] - betta*S[n]*I[n]*dt
          I[i+1] = I[i] + betta*S[i]*I[i]*dt - v*I[i]*dt
          R[i+1] = R[i] + v*I[i]*dt
          
     
     
     plt.plot(time, S, label ="Suscetible")
     plt.plot(time, I, label = "Infected")
     plt.plot(time, R, label = "Recovered")
     plt.legend()
     plt.show()
          



          


