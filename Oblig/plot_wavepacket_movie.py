from numpy import*
import matplotlib.pyplot as p
import glob,os

for line in glob.glob("tmp.png"):
        os.remove(line)

def f(x,t):
        return exp(-(x-3*t)**2)*sin(3*pi*(x-t))

x=linspace(-6,6,1001)
t=linspace(-1,1,61)

count=0
for i in t:
        y=f(x,i)
        p.plot(x,y)
        p.show()
        count=count+1


#This program doesn't show animation it generates a collection of image files
