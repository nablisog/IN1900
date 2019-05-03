import sys
g = 9.81
v0=float(sys.argv[1])
t= float(sys.argv[2])
y = v0*t - 0.5*g*t**2
if t < 0 or t > (2*v0/g):
     print("T doesn't lie between 0 and 2v0/g.")
     sys.exit(2)
print (y)


# or we can use this way
import sys
g = 9.81
try:
    v0= float(sys.argv[1])
    t = float(sys.argv[2])
except IndexError:
    print ("give the values on the command")
    v0 = float(input("value of v0"))
    t = float(input("value of t "))
except ValueError:
    print ("both of them should be numbers")
    sys.exit(1)

if t < 0 or t > 2*v0/g:
    raise ValueError("T doesn't lie between 0 and 2v0/g.")
    sys.exit(1)

y = v*t - 0.5 *g*t** 2
print (y)

"""
Terminal < python3 ball_cml_tcheck.py 4 3
( T doesn't lie between 0 and 2v0/g. )
"""
