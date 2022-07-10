import random
from turtle import Screen, Turtle
import turtle

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")

'''colors = ["CornflowerBlue", "DarkOrchid", "Teal", "HotPink", "IndianRed", "DeepSkyBlue", 
"SeaGreen", "Wheat", "SlateGrey","LightSeaGreen"]'''

'''print(timmy)
timmy.shape("turtle")
timmy.color("darkblue")'''

'''for _ in range(15):
    timmy.fd(10)
    timmy.pu()
    timmy.fd(10)
    timmy.pd()'''


#printshapes
'''def draw_shape(num_of_sides):
    angle = 360 / num_of_sides 
    for _ in range(num_of_sides):
        timmy.fd(100)
        timmy.right(angle)

for shape_side in range(3,10):
    timmy.color(random.choice(colors))
    draw_shape(shape_side)'''

#Generate a random walk
'''directions = [0, 90, 180, 270]
timmy.width(10)
timmy.speed("fastest")


for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.fd(30)
    timmy.setheading(random.choice(directions))'''

#generating random colors
'''directions = [0, 90, 180, 270]
timmy.width(10)
timmy.speed("fastest")


def choose_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(1000):
    timmy.color(choose_color())
    timmy.fd(30)
    timmy.setheading(random.choice(directions))'''

#Drwaing a circle

def choose_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

timmy.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(choose_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(10)




my_screen = Screen()
my_screen.exitonclick()