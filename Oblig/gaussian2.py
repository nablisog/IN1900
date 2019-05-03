from math import sqrt,exp, pi
def gauss(x, m=0, s=1):
     f=1/(sqrt(2*pi)*s) *exp((-0.5)*(((x-m)/s)**2))
     return f
m=0
s=1
n=5
start = m - 5*s
end = m + 5*s
x = [start + i*((end-start)/float(n-1)) for i in range(n) ]
for x in range(0,6):
     print ("%4s %4s " % (x,gauss(x)))
     
"""
Terminal < python3 gaussian2.py
(  0 0.3989422804014327 
   1 0.24197072451914337 
   2 0.05399096651318806 
   3 0.0044318484119380075 
   4 0.00013383022576488537 
   5 1.4867195147342977e-06)
"""






    
