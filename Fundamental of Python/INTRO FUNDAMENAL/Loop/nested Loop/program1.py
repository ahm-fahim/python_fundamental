import turtle

turtle.shape("turtle")
turtle.speed(3)

for side_length in range(100,200,20):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

turtle.exitonclick()