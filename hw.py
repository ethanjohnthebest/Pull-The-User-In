from turtle import *
import time

turtle = Turtle()
screen = Screen()

width = int(input("What width should the pen be? "))
loops = int(input("How many times should the code loop? "))
angle = int(input("What angle should the turn be? "))
for i in range(width):
    time.sleep(1)
    turtle.forward(width)
    turtle.left(angle)
input()