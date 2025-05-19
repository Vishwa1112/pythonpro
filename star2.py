import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
star=turtle.Turtle()

side_length=70
angle=360.0 / 6

for i in range (7):
    star.forward(side_length)
    star.right(angle)

turtle.done()