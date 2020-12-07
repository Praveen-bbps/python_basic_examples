# Indian National Flag
import turtle

# Blue Chakra
turtle.color("#000080")
turtle.pensize(5)
turtle.circle(50)
turtle.left(90)
turtle.forward(50)
for i in range(1,25):
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(15)

turtle.forward(50)
turtle.right(90)
turtle.pensize(3)

# White color at the center
turtle.color("black", "#ffffff")
turtle.forward(225)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(450)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(450)

# Saffron color at the top
turtle.color("black","#f4c430")
turtle.begin_fill()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(450)
turtle.left(90)


turtle.forward(100)
turtle.end_fill()
turtle.forward(100)
# Green color at the bottom
turtle.color("black","#138808")
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(450)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(450)
turtle.end_fill()










    
