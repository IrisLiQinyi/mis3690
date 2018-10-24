import math
class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
jack = Point()
jack.x = 150
jack.y = 100
class circle():
    '''attributes center and radius, 
    where center is a Point object
     and radius is a number
     '''
cir = circle()
cir.center = jack
cir.radius = 75

def point_in_circle(p1):
    '''takes a Circle and a Point 
    and returns True if the Point lies 
    in or on the boundary of the circle.
    '''
    if math.sqrt((150-p1.x)**2+(100-p1.y)**2) <= 75:
        return True
    else:
        return False
# p1 = Point()
# p1.x = 0
# p1.y = 0
# print(point_in_circle(p1))
# print(point_in_circle(p2))

class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """
rec = Rectangle()
rec.width = 100.0
rec.height = 200.0
rec.corner = Point()
rec.corner.x = 150
rec.corner.y = 20

def rect_in_circle(rect):
    '''takes a Circle and a Rectangle and returns True 
    if the Rectangle lies entirely in or on the boundary 
    of the circle 
    '''
    l_l_c = rec.corner
    lower_r_c = Point()
    lower_r_c.x = rec.corner.x + rec.width
    lower_r_c.y = rec.corner.y
    u_l_c = Point()
    u_l_c.x = rec.corner.x
    u_l_c.y = rec.corner.y + rec.height
    u_r_c = Point()
    u_r_c.x = rec.corner.x + rec.width
    u_r_c.y = rec.corner.y + rec.height
    print (l_l_c)
    if point_in_circle(l_l_c) is True and point_in_circle(lower_r_c) is True and point_in_circle(u_l_c) is True and point_in_circle(u_r_c) is True:
        return True 
    else:
        return False

# s = rect_in_circle(rec)
# print ('This is',s)

def rect_circle_overlap(rect):
    '''takes a Circle and a Rectangle and returns True 
    if any of the corners of the Rectangle fall inside the circle
    '''
    l_l_c = rec.corner
    lower_r_c = Point()
    lower_r_c.x = rec.corner.x + rec.width
    lower_r_c.y = rec.corner.y
    u_l_c = Point()
    u_l_c.x = rec.corner.x
    u_l_c.y = rec.corner.y + rec.height
    u_r_c = Point()
    u_r_c.x = rec.corner.x + rec.width
    u_r_c.y = rec.corner.y + rec.height
    if point_in_circle(l_l_c) is True or point_in_circle(lower_r_c) is True or point_in_circle(u_l_c) is True or point_in_circle(u_r_c) is True:
        return True
    else:
        return False

# o = rect_circle_overlap(rec)
# print(o) 

##OOP2
class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

# print(Time())
start = Time()
start.hour = 9
start.minute = 45
start.second =  0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

done = add_time(start, duration)
print('This is ', done)

# Modifier
def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    return time
# print('So', increment(start,30))

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
print (time_to_int(start))

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
print(int_to_time(start))
def add_time_2(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
print(add_time_2(start,duration))

#Error Handling
def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True
print(valid_time(duration))

# def add_time_2(t1, t2):
#     if not valid_time(t1) or not valid_time(t2):
#         raise ValueError('invalid Time object in add_time')
#     seconds = time_to_int(t1) + time_to_int(t2)
#     return int_to_time(seconds)
# print(add_time_2(start,duration))

# def add_time(t1, t2):
#     assert valid_time(t1) and valid_time(t2)
#     seconds = time_to_int(t1) + time_to_int(t2)
#     return int_to_time(seconds)
