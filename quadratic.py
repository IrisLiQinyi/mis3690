import math
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
def quadratic(a,b,c) :
    x1= (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2= (-b-math.sqrt(b**2-4*a*c))/(2*a)
    return x1,x2   
quadratic(a,b,c)
print (quadratic(a,b,c))


