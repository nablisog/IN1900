from matplotlib.pyplot import *  
import  numpy as np
#a
K1=5.01e-7
K2=4.79e-11
pH =np.linspace(4,12,1001)
H=10**-pH
CO2=H**2/(H**2 +(K1*H)+(K1*K2))
HCO3=(K1*H)/(H**2+(K1*H)+(K1*K2))
CO3=(K1*K2)/(H**2+(K1*H)+(K1*K2))

y=CO2,HCO3,CO3
plot(pH,CO2)
plot(pH,HCO3)
plot(pH,CO3)
show()


