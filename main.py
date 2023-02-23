import colorgram
from turtle import Turtle
from random import choice
from turtle import colormode
from turtle import Screen
colours = colorgram.extract("image.jpg", 30)
rgb_colours = []

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_colour = (r, g, b)
    rgb_colours.append(new_colour)

print(rgb_colours)

colour_list = [(255, 255, 255), (243, 234, 76), (211, 158, 93), (188, 12, 69), (111, 179, 208), (25, 116, 169), (172, 172, 31), (221, 128, 166), (160, 78, 35), (128, 186, 146), (10, 32, 76), (235, 73, 41), (217, 67, 108), (31, 135, 83), (176, 48, 95), (234, 165, 194), 
(79, 13, 63)]

# 10x10 rows of spots
# 20 size
# 50 paces between dots

tim = Turtle()
tim.color("white")
r = -225
t = -225
tim.setpos(-225, -225)
tim.color("black")
tim.shape("turtle")
tim.shapesize(1)
tim.speed(1)
tim.pensize(20)
colormode(255)

def draw_circle():
    tim.dot(20, choice(colour_list))
    tim.penup()
    tim.forward(50)

for y in range(10):
    for x in range(10):
        draw_circle()
    tim.setpos(r, t + 50)
    t += 50

screen = Screen()
screen.exitonclick()
 