import turtle 

turtle.speed(5)
turtle.shape("turtle")

for i in range(20):
    turtle.forward(20)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
turtle.exitonclick()