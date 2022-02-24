import turtle 

height = 10
width = 10

turtle.speed(10)
turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(40)
    turtle.backward(40* width)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)

turtle.exitonclick()