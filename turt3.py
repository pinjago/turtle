import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

alex.pensize(10)

for aColor in ["yellow", "red", "lightgreen", "darkblue"]:
    alex.color(aColor)
    alex.forward(50)
    alex.left(90)

wn.exitonclick()