from math import*
n = 5
v0 = 5.0
g = 9.81
t_stop = 2*v0/g
dt = t_stop/n
t1=[]
y1=[]
for i in range(n+1):
    t = i*dt
    y = v0*t-0.5*g*t**2
    t1.append(t)
    y1.append(y)

for a,b in zip(t1,y1):
    print('%4.2f %4.2f' %(a,b))

 """
Terminal < python3 ball_table2.py>(
0.00 0.00
0.20 0.82
0.41 1.22
0.61 1.22
0.82 0.82
1.02 0.00)
"""    
