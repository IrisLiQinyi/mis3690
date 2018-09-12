def my_abss(n):
    if n < 0:
        print(-n)
    else:
        print(n)

my_abss(-5)
my_abss(4)


def give_me_a_break():
    return 'break'

print(give_me_a_break())

type(42)
type('42')
int('hello')

def print_lyrics ():
    print('Hey Jude, dont\'t make it bad.')
    print('Take a sad song and make it better')
type (print_lyrics)
print_lyrics()
def repeat_lyrics ():
    print_lyrics()
    print('Na - na - na - na, na - na - na')
    print_lyrics()
repeat_lyrics()

def print_twice(whatever_name):
    print(whatever_name)
    print(whatever_name)
print_twice('Babson')

#def print_twice(A) :
#    print(A)
#    print(A)
print_twice('Iris')

my_name = 'Jack'
print_twice(my_name)
#Exercise abs
def my_abs(A) :
    print(abs(A))
my_abs(-5)

def cat_twice(a,b) :
    cat = a + b
    print_twice(cat)
line1 = 'Bing tiddle '
line2 = 'tiddle bang'
cat_twice(line1,line2)
#print (cat) cat is only in the function

#def give_me_a_break() :
    #str1 = 'break'
    #return str1
print(give_me_a_break())

#def give_me_a_break() :
str1 = 'break'
    #return str1 #This is when it's stopped
    #print ('another break')
print(give_me_a_break())

#result = print_twice('Bing')
#print(result)

def nop() :
    pass

age = int(input())
if age > 18:
    pass

abs('A')

import math
def move(x,y,step,angle) :
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x,y = move(100,100,60,math.pi/6)
print(x,y)
