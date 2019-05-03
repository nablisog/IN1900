
p=5    
N=4  
x0=100
outfile=open("new.txt", "w")
xnm1=x0
n=0
while n<=N:
	xn=xnm1+(p/100)*xnm1
	xnm1=xn
	outfile.write("After 4 years with 5 percent interest it grew to %.2f" % (xn))
	n=n+1


        

