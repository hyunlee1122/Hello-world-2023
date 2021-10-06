import turtle

circle = turtle.Turtle()
tone = turtle.Screen()

tone.bgcolor("black")
circle.pencolor("#A5A6F6")

a = 0
b = 0
circle.speed(100)
circle.penup()
circle.goto(0, 200)
circle.pendown()

while(True):
    circle.forward(a)
    circle.right(b)
    a += 3
    b += 1

    if b == 150:
        circle.color("#EF5DA8")
    circle.hideturtle()

    if b == 200:
        break
    circle.hideturtle()


turtle.done()
