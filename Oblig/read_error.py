from numpy import*
from matplotlib.pyplot import*
file="lnsum.py"
def error(file):
     with open (file,"r") as infile:
          epislon = []
          error = []
          n =[]
          for line in infile:
               epislon.append(float(line[9:14]))
               error.append(float(line[29:37]))
               n.append(float(line[41:44]))
     return epislon,error,n

epislon,error,n = error(file)
semilogy(n,epislon)
semilogy(n,error)
show()
         
