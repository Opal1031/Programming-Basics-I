n = int(input("나무 크기 : "))

i = 1
size = 2*n + 1

while i <= n:
    j = i
    while j <= 2*i + 1:
        print(" " * (size - j) + "*" * (2*j - 1))
        j += 1
    i += 1