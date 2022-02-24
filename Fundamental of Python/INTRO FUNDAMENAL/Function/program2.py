import turtle 

def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

counter = 0
while counter < 90:
    draw_square(200)
    turtle.right(4)
    counter += 1

turtle.exitonclick()