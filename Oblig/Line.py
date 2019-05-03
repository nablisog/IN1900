class Line:
     
     def __init__(self,p1,p2):
          x0,x1=p1
          y0,y1=p2
          self.z=(y1-y0)/(x1-x0)
          self.z1=(x1*y0 - x0*y1)/(x1-x0)

     def caller(self,x):
          return self.z + self.z1


def Line_test():
     x=0.5
     l = Line((0,-1), (2,4))
     tol=1e-14
     
     expected=0.25
     computed=l.caller(x)
     diff=abs(computed - expected) < tol
     msg = expected,computed
     success=expected==computed
     assert success,msg

Line_test()
