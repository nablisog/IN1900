from numpy import*
class Quadratic:

     def __init__ (self,a,b,c):
          self.a=a
          self.b=b
          self.c=c
         
     def value(self,x):
          a,b,c=self.a,self.b,self.c
          return a*x**2 + b*x + c
          
     def table(self,l,r,n):
          x_values=linspace(l,r,n)
          for line in x_values:
               print(line,self.value(line))

     def roots(self):
          d=sqrt((b**2) - 4*a*c)
          d1=(-b+d)/(2*a)
          d2=(-b-d)/(2*a)
          return d1,d2
          
q=Quadratic(2,4,2)
print(q.table(-2,2,4))
print(q.value(0))
print(q.value(10))
             

