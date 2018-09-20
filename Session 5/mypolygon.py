import turtle
import math
jack = turtle. Turtle()

# turtle.mainloop()

#for i in range(4):
    #print ('Hello!')

#for i in range(4):
 #   jack.fd(100)
 #   jack.lt(90)

def square(t,length):
    '''Draws a square
    '''
    for i in range(4):
        t.fd(length)
        t.lt(90)

jack = turtle.Turtle()

#square(jack,100)

def polygon(t,length,n):
    for i in range (n):
        t.fd(length)
        t.lt(360/n)

jack = turtle.Turtle()
#polygon(jack,10,10)


def circle(t,r):
    circumference = 2 * math.pi *r
    n = 20
    length = circumference / 3
    polygon(t,length,3)
jack = turtle.Turtle()
#circle(jack,150)

polygon(t=jack,n=7,length=70) #when using key words we can change the position

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
# arc(jack, 100, 270)
turtle.mainloop()


