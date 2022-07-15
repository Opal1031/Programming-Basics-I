import turtle

speed = 10

turtle.speed()
turtle.bgcolor("black")
colors = "red blue yellow green purple".split()

n = int(input("Input a number (3~5) "))
x = 0

while x < 250:
    turtle.color(colors[x % n])
    turtle.forward(x * 2)
    turtle.left(360 / n - 1)
    x += 1