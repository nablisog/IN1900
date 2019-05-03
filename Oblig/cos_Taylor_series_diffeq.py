from math import*
from numpy import*
def cos_taylor(x,n):
     a=zeros(n+2)
     s=zeros(n+2)
     a[0]=x
     for j in range(1,n+2):
          a[j]=-x**2/((2*j+1)*(2*j)*a[j-1])
          s[j]=s[j-1]+a[j-1]
     
     return s[n+1],abs(a[n+1])
cos_taylor(pi/2,40)

from math import factorial              
def cos_taylor_test():
     x=3*pi/2
     n=2
     tol=1e-14
     
     expected = x-(x**3)/factorial(3)+(x**5)/factorial(5)
     computed = cos_taylor(x,n)[0]
     success = abs(expected-computed) < tol
     msg="Message shown if test fails"
     assert success, msg

cos_taylor_test()
   


