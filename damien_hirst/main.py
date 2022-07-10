# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)

import random
import turtle
from turtle import Turtle

turtle.colormode(255)

wes = Turtle()

color_list = [(43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253), (160, 3, 82), (4, 211, 101), (3, 138, 64),
              (246, 42, 127), (109, 108, 247), (252, 253, 53), (184, 184, 251), (211, 106, 5), (35, 35, 252),
              (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56), (216, 114, 171), (16, 127, 144),
              (85, 248, 252), (188, 39, 109), (23, 5, 107), (8, 209, 215), (99, 8, 50), (231, 163, 205), (204, 119, 35),
              (112, 6, 4), (239, 165, 161), (8, 114, 21)]
wes.penup()
wes.hideturtle()
wes.speed("fastest")

wes.setheading(225)
wes.fd(300)
wes.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    wes.dot(20, random.choice(color_list))
    wes.forward(50)

    if dot_count % 10 == 0:
        wes.setheading(90)
        wes.fd(50)
        wes.setheading(180)
        wes.fd(500)
        wes.setheading(0)

my_screen = turtle.Screen()
my_screen.exitonclick()
