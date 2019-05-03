from random import*
import sys
n = int(sys.argv[1])
N = int(sys.argv[2])

def dice(n, N):         
     counter = 0
     for i in range(N):
          for j in range(n):
               r = randint(1,6)
               if r == 6:
                    counter +=1
                    

     return counter/N
                    
Monte = 11/36
for i in range(N):
     x, y = dice(n, i)
     print(n, i, x, y, Monte)

#i try different ways but i get only this answer
"""
Termianla:-
File "one6_ndice.py", line 15, in dice
    return counter/N
ZeroDivisionError: division by zero

"""
