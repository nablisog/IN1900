from math import*
v0 = 5.0
g = 9.81
n = 5
t_stop = 2*v0/g
dt = t_stop/n
t = [i*dt for i in range(0,n+1)]
y = [v0 * t[i] - 0.5 * g * t[i] **2 for i in range(0, n+1)]

ty1=[t, y]
for i in range (len(t)):
    print ("%4.2f %4.2f" % (ty1[0][i], ty1[1][i]))

ty2 = [[t[i], y[i]] for i in range(n+1)]

for i in range(n+1):
    print ("%4.2f %4.2f" % (ty2[i][0], ty2[i][1]))

"""
Terminal < python3 ball_table3.py>(
0.00 0.00
0.20 0.82
0.41 1.22
0.61 1.22
0.82 0.82
1.02 0.00
0.00 0.00
0.20 0.82
0.41 1.22
0.61 1.22
0.82 0.82
1.02 0.00)
"""    





