import turtle
import random

screen = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')
t.shapesize(3,3,2)
t.color('black','brown')
t.pu()
t.speed(0)

p = turtle.Turtle()
p.shape('circle')
p.shapesize(3,3,2)
p.color('black','red')
p.pu()
p.speed(0)

def food():
    p.goto(random.randrange(-160, 160, 10), random.randrange(-160, 160, 10))
    screen.ontimer(food, 10000)
    
def up():
    t.setheading(90)
    t.forward(10)

def down():
    t.setheading(270)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def right():
    t.setheading(0)
    t.forward(10)

turtle.listen()
turtle.onkey(up, "w")
turtle.onkey(down, "s")
turtle.onkey(left, "a")
turtle.onkey(right, "d")

food()
