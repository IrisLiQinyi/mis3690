import math
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
def quadratic(a,b,c) :
    x1= (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2= (-b-math.sqrt(b**2-4*a*c))/(2*a)
    return x1,x2  #throw the result outside the funciton  
quadratic(a,b,c)
print (quadratic(a,b,c))

#from math import sqrt 
#sqrt()
#or
#import math
#math.sqrt()


