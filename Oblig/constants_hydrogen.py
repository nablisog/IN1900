#A
with open("sun.txt","r") as infile:
     infile.readline()
     infile.readline()
     distance={}
     mass={}
     radius={}
     for line in infile:
          x=line.split()
          a=x[0]
          b=float(x[1])
          c=float(x[2])
          d=int(x[3])
          distance[a]=b
          mass[a]=c
          radius[a]=d
print(distance)
print(mass)
print(radius)    
#B
from math import*
with open("sun.txt","r") as infile:
     infile.readline()
     infile.readline()
     distance={}
     mass={}
     radius={}
     densities={}
     for line in infile:
          x=line.split()
          a=x[0]
          b=float(x[1])
          c=float(x[2])
          d=int(x[3])
          d=d*1000
          distance[a]=b
          mass[a]=c
          radius[a]=d
          v=(4/3) * pi * (d**3)
          den=c/v
          densities[a]= den

print(densities)


