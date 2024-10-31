import turtle

#function to draw a squircle
def draw_squircle(size, corners):
    turtle.speed(0)
    for i in range(corners):
        turtle.forward(size)
        turtle.right(90 - (90/corners)) #this adjusts the angle to make a rounded corner

#set up the screen and turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.pencolor("white")

#draw a squircle
draw_squircle(100,100) #size and the number of corners/steps for smoothness

#hide the turtle
turtle.hideturtle()

#keep the window open
turtle.done()