def f(n):
     if n == 0:
          return 1
     if n < 0:
          print("invalid")
     res = 1
     for i in range(2,n+1):
          res = res*i
     return res

print(f(5))
          
          
