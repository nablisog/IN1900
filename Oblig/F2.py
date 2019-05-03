from math import pi,exp,sin
class F:
     def __init__(self,a,w):
          self.a=a
          self.w=w

     def value(self,x):
          return exp(-self.a*x)*sin(self.w*x)

     def caller(self):
          return "exp(-a*x)*sin(w*x)"


f=F(a=1,w=0.1)
p=f.value(x=pi)
print(p)
f.a=2
q=f.value(pi)
print(q)
print(f.caller())

