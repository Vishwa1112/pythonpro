import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
square=turtle.Turtle()

side_length=70
angle=360.0 / 6

for i in range (7):
    square.forward(side_length)
    square.right(angle)

turtle.done()