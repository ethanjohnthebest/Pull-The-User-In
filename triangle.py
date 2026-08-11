from turtle import *
import time

turtle = Turtle()
screen = Screen()

"""
It can make any shapes just types what it is asking for
"""
loop = 3
pixels = 160
degree = 120
for i in range(loop):
    time.sleep(1)
    turtle.forward(pixels)
    turtle.left(degree)
input()