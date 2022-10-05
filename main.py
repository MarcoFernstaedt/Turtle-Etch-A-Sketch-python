from turtle import Turtle


from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_up():
    timmy.setheading(90)
    timmy.fd(10)

def move_down():
    timmy.setheading(270)
    timmy.fd(10)

def move_left():
    timmy.setheading(190)
    timmy.fd(10)

def move_right():
    timmy.setheading(0)
    timmy.fd(10)

screen.listen()
screen.onkey(key='w', fun=move_up)
screen.exitonclick()