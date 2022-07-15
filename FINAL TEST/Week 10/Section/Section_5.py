import turtle

angle = 360 * 8
angleStep = 36
r = 80

while r:
    turtle.circle(r, angleStep)
    r -= 1

turtle.clear()

i = 3
while i < 8:
    turtle.circle(i * 10, steps = i)
    i += 1

input()