import turtle

def draw_triangle(arm):
    for i in range(3):
        turtle.forward(arm)
        turtle.left(120)

counter = 0
while counter < 1:
    draw_triangle(200)
    counter += 1

turtle.exitonclick()
    
