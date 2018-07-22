from turtle import *
import random

xmax = 250
xmin = -250
ymax = 250
ymin = -250
proximity = 10

def sensor():
    if xmax - position()[0] < proximity:
        #Too close to right wall
        return True
    if position()[0] - xmin < proximity:
        #Too close to left wall
        return True
    if ymax - position()[1] < proximity:
        #Too close to top wall
        return True
    if position()[1] - ymin < proximity:
        #Too close to bottom wall
        return True
    #Not too close to any
    return False

def straightLine():
    left(random.randrange(0,360))
    while not sensor():
        forward(1)

def spiral(gap = 10):
    current_radius = gap
    while not sensor():
        circumference = 2 * 3.14159 * current_radius
        fraction = 1/circumference
        left(fraction * 360)
        forward(1)
        current_radius += gap * fraction

def followwall():
    xRange = random.randint(-240, 240)
    yRange = random.randint(-240, 240)
    penup()
    my_start = setposition(xRange, yRange)
    min = xmax - position()[0]
    setheading(90)
        #closest to right wall
    if position()[0] - xmin < min:
        min = position()[0] - xmin
        setheading(270)
        #closest to left wall
    if ymax - position()[1] < min:
        min = ymax - position()[1]
        setheading(180)
        #closest to top wall
    if position()[1] - ymin < min:
        #closest to bottom wall
        setheading(0)

    while not sensor():
        pendown()
        forward(1)


def BackupSpiral(backup = 50, gap = 20):
    while not sensor() and backup > 0:
        backward(1)
        backup -= 1
    spiral(gap)



def explore():
    speed(0)
    spiral(40)
    while (True):
        backward(1)
        which_function = random.choice(['a', 'b', 'c'])
        if which_function == 'a':
            straightLine()
        if which_function == 'b':
            BackupSpiral(random.randrange(100, 200), random.randrange(10, 50))
        if which_function == 'c':
            followwall()

explore()


