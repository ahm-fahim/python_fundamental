import turtle

turtle.shape("turtle")
turtle.speed(5)

for i in range(2):
    for i in range(1):
        turtle.forward(600)
        turtle.left(90)
    turtle.forward(300)
    turtle.left(90)


turtle.exitonclick()