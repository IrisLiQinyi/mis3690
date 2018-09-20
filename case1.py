# import turtle
# jack = turtle.Turtle()
# #print (jack)
# # jack.fd(100)
# # jack.lt(90)
# # jack.fd(100)

# # def square(t,length):
# #     for i in range (4):
# #         t.fd(length)
# #         t.lt(90)
# # square (jack,100)

# def polygon(t,length,n):
#     n = int(n)
#     angle = 360/n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
# # polygon (jack,100,6)

# import math
# # def circle(t,r):
# #     circumference = 2* math.pi * r
# #     n = 50
# #     length = circumference / n
# #     polygon(t,n,length) 

# # circle(jack,50)

# def circle(t,r):
#     circumference = 2 * math.pi * r
#     n = int(circumference/3)+1
#     length = circumference/n
#     polygon(t,n,length)
# circle(jack,60)

# turtle.mainloop()



# # for i in range (4):
# #     print ('Hello')
# import turtle
# import math
# jack = turtle.Turtle()
# def arc(t,r,angle):
#     arc_length= 2*math.pi*r*angle/360
#     n= int(arc_length/3) + 1
#     step_length= arc_length /n
#     step_angle= angle/n

# for i in range (n):
#     t.fd(step_length)
#     t.lt(step_angle)
# arc(jack,5,30)
# turtle.mainloop()

import turtle
import math
jack = turtle.Turtle()
def polyline(t,n,length,angle):
    '''Draws n line segments with the given strength 
    and angle in degrees between them. 
    t is a turtle'''
    for i in range(n):
        t.fd(length)
        t.lt(angle)
#polyline(jack,3,100,40)

# def polygon(t,n,length):
#     angle = 360.0/n 
#     polyline(t,n,length,angle)
#polygon(jack,5,100)

def arc(t,r,angle):
    arc_length=2*math.pi*r*angle/360
    n =int(arc_length/4)+1
    step_length=arc_length/n
    step_angle=float(angle)/n
    polyline(t,n,step_length,step_angle)
# arc(jack,50,100)

def circle(t,r):
    arc(t,r,360)
#Exercise 1
# circle(jack,50)
# jack.lt(60)
# arc(jack,50,120)
# jack.lt(120)
# arc(jack,50,120)
# jack.lt(120)
# arc(jack,50,120)
# jack.lt(60)
# arc(jack,50,60)
# jack.lt(60)
# arc(jack,50,120)
# jack.lt(120)
# arc(jack,50,120)
# jack.lt(120)
# arc(jack,50,120)
# turtle.mainloop()

#Exercise 2
circle(jack,100)
jack.lt(60)
circle(jack,50)

turtle.mainloop()
