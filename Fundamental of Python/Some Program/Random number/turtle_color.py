import turtle
import random

#list of color

colors = ["red","green", "blue", "yellow", "orange", "black", "purple"]

turtle.penup()

for i in range(50):
    x = random.randint(-300,300)
    y = random.randint(-300,300)

    #set random position
    turtle.setposition(x,y)
    #set random color
    i = random.randint(0,len(colors)-1)
    turtle.dot(colors[i])

turtle.done()