from turtle import Turtle, Screen

wes = Turtle()
screen = Screen()


def forward():
    wes.fd(10)

def backwards():
    wes.backward(10)

def counter_clockwise():
    wes.left(10)

def clockwise():
    wes.right(10)

def clear_drawing():
    wes.clear()
    wes.penup()
    wes.home()
    wes.pendown()
    






screen.listen()
screen.onkey(forward, "w")
screen.onkey(backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()