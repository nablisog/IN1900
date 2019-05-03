class Rectangle:
     
     def __init__ (self,w,h,x0,y0):
          self.w=w
          self.h=h
          self.x0=x0
          self.y0=y0

     def area(self):
          return self.w * self.h

     def parameter(self):
          return 2*(self.h + self.w)

from math import sqrt
class Triangle:
     
     def __init__ (self,v1,v2,v3):
          self.v1=v1
          self.v2=v2
          self.v3=v3

     def area(self):
          x0, y0= self.v1
          x1, y1= self.v2
          x2, y2 =self.v3
          a = 0.5 * abs(x1*y2 - x2*y1 - x0*y2 + x2*y0 + x0*y1 - x1*y0)
          return a

     def parameter(self):
          x0, y0= self.v1
          x1, y1= self.v2
          x2, y2 =self.v3
          p=sqrt((x1-x0)**2+(y1-y0)**2)+sqrt((x2-x0)**2+(y2-y0)**2)+sqrt((x2-x1)**2+(y2-y1)**2)
          return p

r=Rectangle(4,4,4,4)
t=Triangle((0,0),(2,0),(2,4))


def rectangel_test():
     w=4;h=4;x0=4;y0=4
     tol=1e-14
     r = Rectangle(w,h,x0,y0)
     expected_area = w*h
     computed_area = r.area()
     diff=abs(expected_area - computed_area) < tol
     msg =expected_area,computed_area
     success= computed_area==expected_area
     assert success,msg

rectangel_test()

def rec_para_test():
     w=4;h=4;x0=4;y0=4
     tol=1e-14
     r = Rectangle(w,h,x0,y0)
     expected_p = 2*(w+h)
     computed_p = r.parameter()
     diff=abs(expected_p - computed_p) < tol
     msg =expected_p,computed_p
     success= computed_p==expected_p
     assert success,msg
     
rec_para_test()          


def triangel_test():
     t=Triangle((0,0),(2,0),(2,4))
     if t.area() == 4:
          success = True
     else:
          False
     msg = "Message shown if test fails"
     assert success, msg
     
triangel_test()

    
          
          
          
          
          

     
     
          

          
     
