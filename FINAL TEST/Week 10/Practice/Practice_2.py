import turtle

def star():
    turtle.forward(190)
    turtle.left(144)

turtle.circle(100)
turtle.left(72)
for i in range(0,5):
    star()

input()