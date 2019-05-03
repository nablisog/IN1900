from math import*
Q= 1.2                 #kg m^3 density 
a=0.11                 #m 
A = pi*a**2            # cross-sectional area
V_1=120/3.6            #changing from km/hr to m/s velocity1 =120*(1000/3600)
V_2=30/3.6             #changing from km/hr to m/s velocity2 =30*(1000/3600) 
CD = 0.4               #the drag coefficient 
g = 9.81               #gravity m s^2
m = 0.43               #mass kg
fg= m*g                #gravity force
fd1=0.5*CD*Q*A*V_1**2  #when it's kicked hard
fd2=0.5*CD*Q*A*V_2**2  #when it's kicked soft
ratio= fd1*fg          #ratio of the drag force when its kicked hard
r_2= fd2*fg            #ratio of the drag force when its kicked soft

print (" Gravity force:" ,fg)
print (" Hard kick:" , fd1)
print (" Soft kick:" , fd2)
print (" Ratio when kicked hard:" , ratio)
print (" Ratio when kicked soft:" , r_2)


"""
Terminal < python3 kick.py>
(Gravity force: 4.2183
 Hard kick: 10.136872295583068
 Soft kick: 0.6335545184739417
 Ratio when kicked hard: 42.760368404458056
 Ratio when kicked soft: 2.6725230252786285)
"""
