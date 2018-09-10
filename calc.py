age=int(input('Please enter your age:'))

if age > 21:
    print ('Yes, you can.')
else:
    print ('Sorry, you cannot.')
a=3
type(a+2)

print ('Hello, World!')
print ('Hey Jude', 'don\'t make it bad')
print ('The total number of overall medals in Rio 2016 is', 46+37+38)
print ('46 + 37 + 38 =', 47+36+38)
name = input()
name
print (name)

name = input('Enter your name: ')
print ('Hello, ', name)

message ='I did something cool today!'
print (message)

n=100
print (n)

a=123
print (a)

a = 'ABC'
b=a
a='XYZ'
print(b)

'Hello, {}'. format('world')
'Congratulations, {:s}, you won {:d}th Academy award.' .format('Gary Oldman',90)
'Today is {:d}/{:d}' .format (9,4)
print('Pi equals {:8.5f}.' .format(3.1415926))
print('Age:{}. Gender:{}' .format(20, True))
print('Growth rate:{:.2f}%' .format(7))
print('Coordinates: {latitude},{longitude}' .format(latitude='42.30N', longitude='71.27W'))
print('{0}, {1}, {2}'.format('a','b', 'c'))
print('{2}, {1}, {0}' .format('a', 'b', 'c'))

#Homework
#1
r=input('What is r?')
import math
V = ((4/3)*math.pi*r**3)
print(V)

pi=3.1415926
r = 5
v = (4/3)*pi*r**3
print(v)

#2
p = 24.95 * 0.40 #cover price
s = 3 + 0.75*59 #shipping cost
t = p + s #Total cost
print(t)

#3
t_1=8+15/60 #first mile
t_2=7*3+3*12/60 # the nest 3 miles
t_3=8+15/60 # last mile
total = t_1+t_2+t_3 #total minutes
tfb = total - 8 #min after 7
print ('7:{:.0f}' .format(tfb))

#4
percentage = (89-82)/89
print('{:.1f}%' .format(percentage*100))

46+37+38

# Exercise 2
#1
s = 42*60 + 42
print(s)

#2
m = 10/1.61
print (m)

#3/1
ap = 2562/6.2
ap_m = ap/60
print ('{}min,{}sec' .format(int(ap_m),ap_m-int(ap_m)))
#3/2
a_s= 6.2/(2562/3600)
print (a_s)