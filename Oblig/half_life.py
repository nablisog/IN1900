import math
from math import*
N=4.5
t=10*60
mean_life=1760
remain=N*exp(-t/mean_life)
print (remain)

mean_life=(t*0.5)/(log(2))
remain=N*exp(-t/mean_life)
print(remain)

N=4.5
t=10*60
half_life =1220/(log(2))
remain=N*exp(-t/half_life)
print (remain)

"""
Terminal < python3 half_life.py>
(3.200
1.125
3.200)
"""

