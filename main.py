from turtle import Turtle


from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_up():
    timmy.setheading(90)
    timmy.fd(10)

def move_down():
    pass

def move_left():
    pass

def move_right():
    pass

screen.listen()
screen.onkey(key='w', fun=move_up)
screen.exitonclick()