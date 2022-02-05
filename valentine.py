import turtle 
from turtle import *

def curvemove():

    for i in range(200):

        right(1)

        forward(1)

turtle.title("Happy Valentine's Day")#Set title for image

turtle.pensize(width=5)#stroke width

color("red","pink")#Brush color and fill color

begin_fill()

left(140)#Rotate 140 degrees counterclockwise

turtle.speed(1.5)#Line speed

forward(111.65)#Forward travel 111.65

curvemove()#Call the curvemove function

left(120)

curvemove()

turtle.speed(1.5)

forward(111.65)

end_fill()

turtle.up()#Stop drawing

left(230)

forward(75)

turtle.write("I LOVE YOU ",align="Center",font=("Arial", 16, "normal"))

right(180)

forward(120)

turtle.write("Happy Valentine's Day ",align="Center",font=("Arial", 16, "normal"))

turtle.hideturtle()

done()