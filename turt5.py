import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.pensize(15)
alex.color("green")
alex.circle(50)

alex.color("yellow")
alex.penup()
alex.setposition(-120, 0)
alex.pendown()
alex.circle(50)

alex.color("pink")
alex.penup()
alex.setposition(60,60)
alex.pendown()
alex.circle(50)

alex.color("black")
alex.penup()
alex.setposition(-60,60)
alex.pendown()
alex.circle(50)

alex.color("blue")
alex.penup()
alex.setposition(-180, 60)
alex.pendown()
alex.circle(50)

wn.exitonclick()

