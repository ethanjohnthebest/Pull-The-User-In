from turtle import *
import time

turtle = Turtle()
screen = Screen()

"""
It can make any shapes just types what it is asking for
"""
loop = int(input("how many times should i loop ??? "))
pixels = int(input("how many pixels should i move forward ??? "))
degree = int(input("how many degree should i move turn left ??? "))
for i in range(loop):
    time.sleep(1)
    turtle.forward(pixels)
    turtle.left(degree)
input()