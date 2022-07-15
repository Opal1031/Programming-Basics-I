import turtle

angle = 20
i = 0

while i < 360:
    turtle.circle(30)
    turtle.left(angle)
    i += angle

turtle.clear()

angle = 10
i = 0

while i < 360:
    turtle.circle(i // 2)
    turtle.left(angle)
    i += angle