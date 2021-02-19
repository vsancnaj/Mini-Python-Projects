from turtle import *
from random import *
import turtle
import time

# screen set up
setup(800,500)
title("Turtle Race")
bgcolor("forestgreen")
speed(0)

# heading
penup()
goto(-100,205)# (x,y)
color("white")
write("Turtle Race", font = ("Arial", 20, "bold"))

# dirt/ground
goto(-350,200)
pendown()
color("brown")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill() # fill in the track

# finish line
gap_size = 20
shape("square")
penup()

# white squares row 1
color("white")
for i in range(10):
    goto(250,(170 - (i * gap_size * 2)))
    stamp()

# white squares row 2
for i in range(10):
    goto(250 + gap_size,(210- gap_size)-(i * gap_size * 2))
    stamp()

# black squares row 1
color("black")
for i in range(10):
    goto(250,(210- gap_size)-(i * gap_size * 2))
    stamp()

# black squares row 2
color("black")
for i in range(10):
    goto(250+gap_size,(170 - (i * gap_size * 2)))
    stamp()
penup()
# turtle 1 - blue
blue_t = Turtle()
blue_t.color("cyan")
blue_t.shape("turtle")
blue_t.shapesize(1.5)
blue_t.penup()
blue_t.goto(-300, 150)
blue_t.pendown()

# turtle 1 - pink
pink_t = Turtle()
pink_t.color("magenta")
pink_t.shape("turtle")
pink_t.shapesize(1.5)
pink_t.penup()
pink_t.goto(-300, 50)
pink_t.pendown()

# turtle 1 - yellow
yellow_t = Turtle()
yellow_t.color("yellow")
yellow_t.shape("turtle")
yellow_t.shapesize(1.5)
yellow_t.penup()
yellow_t.goto(-300, -50)
yellow_t.pendown()

# turtle 1 - green
green_t = Turtle()
green_t.color("lime")
green_t.shape("turtle")
green_t.shapesize(1.5)
green_t.penup()
green_t.goto(-300, -150)
green_t.pendown()


# pause for 1 second before racing
time.sleep(1)

# move the turtles
while blue_t.xcor() <= 230 and pink_t.xcor() <= 230 and yellow_t.xcor() <= 230 and green_t.xcor() <= 230:
    blue_t.forward(randint(1,10))
    pink_t.forward(randint(1, 10))
    yellow_t.forward(randint(1, 10))
    green_t.forward(randint(1, 10))

# celebrate the winner
# blue turtle wins
if blue_t.xcor() > pink_t.xcor() and blue_t.xcor() > green_t.xcor() and blue_t.xcor() > yellow_t.xcor():
    penup()
    goto(-150, -205)  # (x,y)
    color("cyan")
    write("Winner is Blue turtle!", font=("Arial", 20, "bold"))
    hideturtle()
    for i in range(72):
        blue_t.right(5)
        blue_t.shapesize(2.5)
# pink turtle wins
elif pink_t.xcor() > blue_t.xcor() and pink_t.xcor() > green_t.xcor() and pink_t.xcor() > yellow_t.xcor():
    penup()
    goto(-150, -205)  # (x,y)
    color("magenta")
    write("Winner is Pink turtle!", font=("Arial", 20, "bold"))
    hideturtle()
    for i in range(72):
        pink_t.right(5)
        pink_t.shapesize(2.5)
# yellow turtle wins
elif yellow_t.xcor() > blue_t.xcor() and yellow_t.xcor() > green_t.xcor() and yellow_t.xcor() > pink_t.xcor():
    penup()
    goto(-150, -205)  # (x,y)
    color("yellow")
    write("Winner is Yellow turtle!", font=("Arial", 20, "bold"))
    hideturtle()
    for i in range(72):
        yellow_t.right(5)
        yellow_t.shapesize(2.5)
# green turtle wins
else:
    penup()
    goto(-150, -205)  # (x,y)
    color("lime")
    write("Winner is Green turtle!", font=("Arial", 20, "bold"))
    hideturtle()
    for i in range(72):
        green_t.right(5)
        green_t.shapesize(2.5)


