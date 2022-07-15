import turtle

n = 5
i = 0

while i < n:
    turtle.fd(100)
    turtle.left(720/n)
    i += 1

turtle.clear()

n = 5

while i < n * 5:
    turtle.fd(i  * 10)
    turtle.left(720/n)
    i += 1

input()