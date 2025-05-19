import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()

side_length=70
angle=360.0 / 6

for i in range (7):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()