
def H(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1

def test_H():
    x = [-10,-1e-15, 0, 1e-15,10]                 
    expected = [0,0,1,1,1]          
    computed = H(x)
    success = computed == expected  
    msg = 'computed %s, expected %s' % (computed, expected)
    assert success, msg

"""
Terminal < python3 Heaviside.py
( Nothing comes out so it means that all tests pass )
"""
