import turtle

turtle.shape("turtle")
turtle.speed(5)

for i in range(4):
    turtle.forward(100)
    turtle.left(90)
    for i in range(2):
        turtle.forward(300)
        turtle.left(90)

turtle.exitonclick()