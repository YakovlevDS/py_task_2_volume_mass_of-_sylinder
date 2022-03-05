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

print('Volume of cylinder: ',volume(),'centimeter сubic')