from turtle import Turtle


from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.fd(10)

def move_backwards():
    timmy.bk(10)

def move_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def move_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='space', fun=clear)

screen.exitonclick()