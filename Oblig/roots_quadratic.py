import cmath
def roots(a,b,c):
     x= (b**2) -( 4*a*c)
     y=(-b+cmath.sqrt(x))/(2*a)
     z= (-b-cmath.sqrt(x))/(2*a)
     return y,z
     
def test_roots_float():
     a = 1
     b = 2
     c = 1
     expected = [(-1+0j), (-1+0j)]          
     computed = roots(a,b,c)
     success = computed == expected  
     msg = 'computed %s, expected %s' % (computed, expected)
     assert success, msg

def test_roots_complex():
     a = 1
     b = -2
     c = 3
     expected = [(1+1.4142135623730951j), (1-1.4142135623730951j)]          
     computed = roots(a,b,c)
     success = computed == expected  
     msg = 'computed %s, expected %s' % (computed, expected)
     assert success, msg

print (roots(1,2,1))
print (roots(1,-2,3))

"""
Terminal < python3 roots_quadratic.py
((-1+0j), (-1+0j))
((1+1.4142135623730951j), (1-1.4142135623730951j))
"""
