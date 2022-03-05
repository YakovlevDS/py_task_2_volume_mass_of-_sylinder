import math
PI =math.pi
def radius():
    n=float(input('Diameter cylinder in centimeter: '))
    n/=2
    return n

def height():
    m=float(input('Height cylinder in centimeter: '))
    return m

def volume():
    r=radius()
    h=height()
    s=PI*r**2
    v=s*h
    return v 

def massa(g):
    n=float(input('Specific gravity cylinder in gramm/centimeter сubic: '))
    return g*n/1000 

v= volume()
print('Volume of cylinder: ',v,'centimeter сubic')
print('Massa of cylinder: ',massa(v),'centimeter сubic')