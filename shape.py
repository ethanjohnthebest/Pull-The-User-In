from turtle import *
import time

turtle = Turtle()
screen = Screen()

def make_shape(loop,pixel,angle):

    """
    It can make any shapes just types what it is asking for
    """

    for i in range(loop):   
        time.sleep(1)
        turtle.forward(pixel)
        turtle.left(angle)

make_shape(loop=4,pixel=135,angle=90)
make_shape(loop=3,pixel=135,angle=120)

input()