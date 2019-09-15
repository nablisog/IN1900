
from math import sin

def half_life(x):
     if sin(x) > 0:
          return sin(x)
     else:
          return 0
     
    

print(half_life(0))


def test_half_life():
     x = 0
     expected = 0
     computed = half_life(x)
     tol = 1E-11
     success = abs(expected-computed)<tol
     msg = 'expected %g, computed %g' %(expected,computed)
     assert success, msg

     
test_half_life()
