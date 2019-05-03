from random import*
def probability(N):
     counter=0
     for i in range(N):
          r = random()
          if r >= 0.5 and r <= 0.6:
               counter+=1
     return counter, counter/float(N)

for i in [1,2,3,6]:
     N = 10**i
     print(N,probability(N))

"""
Terminal:-:python python3 compute_prob.py
10 (0, 0.0)
100 (10, 0.1)
1000 (89, 0.089)
1000000 (99780, 0.09978)

"""         







     



     
