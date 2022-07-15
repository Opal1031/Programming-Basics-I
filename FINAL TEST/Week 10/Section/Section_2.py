import turtle

n = int(input("Input a number : "))
i = 0

while i < n:
    turtle.fd(100)
    turtle.left(360/n)
    i += 1

input()