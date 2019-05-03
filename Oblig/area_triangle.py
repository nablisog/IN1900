
def area(vertices):
     x1,y1= vertices[0]
     x2,y2= vertices[1]
     x3,y3= vertices[2]
     a= 0.5 * abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)
     return a

v1=(0,0)  
v2=(1,0)
v3=(0,2)
vertices =[v1,v2,v3]

triangel=area(vertices)
print (triangel)

"""
Terminal < python3 area_triangle.py
( 1.00 )
""" 

     
    
