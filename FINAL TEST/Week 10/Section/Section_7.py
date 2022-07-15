import turtle

def drawCircle(x, y, color):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.color(color)
    turtle.circle(50)

turtle.shape("turtle")
turtle.pensize(5)
turtle.speed(10)

drawCircle(-80, 70, "blue")
drawCircle(0, 70, "black")
drawCircle(80, 70, "red")
drawCircle(-40, 0, "yellow")
drawCircle(40, 0, "green")

input()