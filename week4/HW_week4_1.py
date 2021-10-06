import turtle
import random

turtle.bgcolor("#191919")
turtle.color("#ffffff")

robot = turtle.Turtle()
turtle.speed(800)
myDirectionFun = [turtle.forward, turtle.right,
                  turtle.left, turtle.back, turtle.circle, turtle.dot]
myColor = ["#EF5DA8", "#F178B6", "#FCDDEC", "#A5A6F6", "#7879F1", "#5D5FEF"]


while True:
    r = random.randint(0, 80)
    turtle.color(random.choice(myColor))
    random.choice(myDirectionFun)(r)
turtle.exitonclick()
