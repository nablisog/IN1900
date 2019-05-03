
#using while loop
f=0
df=10
while f<=100:
     c=(f-32)*5/9
     app_c=(f-30)/2
     print ("%4d %6.2f %4d"% (f, c,app_c))
     f=f+df

# using for loop     
 
f=0   
for i in range(0,101,10):
     c=(f-32)*5/9
     app_c=(f-30)/2
     print ("%4d %6.2f %4d " % (f,c,app_c))
     f=f+df


"""
Terminal < python3 f2c_approx_table.py
(  0 -17.78  -15
  10 -12.22  -10
  20  -6.67   -5
  30  -1.11    0
  40   4.44    5
  50  10.00   10
  60  15.56   15
  70  21.11   20
  80  26.67   25
  90  32.22   30
 100  37.78   35)
"""
     
     
     
