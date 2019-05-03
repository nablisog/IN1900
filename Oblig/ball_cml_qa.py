import sys
try:
     v0=float(sys.argv[1])
     t= float(sys.argv[2])
except IndexError:
     print(" Put values on the command")
     v0=float(input(" value of v0 "))
     t= float(input(" value of t "))
          
except ValueError:
     print("Both must be pure numbers")
     sys.exit(1)
g = 9.81
y = v0*t - 0.5*g*t**2
print (y)

"""
Terminal < python3 ball_cml_qa.py
( Put values on the command
   value of v0 4
   value of t 3
  -32.145 )
"""
