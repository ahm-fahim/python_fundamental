import turtle
import random

turtle.penup()

for i in range(50):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.setposition(x,y)
    turtle.dot()

turtle.done()
