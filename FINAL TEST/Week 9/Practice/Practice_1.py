def Cal_Zero():
    i = 2
    while i <= 9:
        j = 1
        while j <= 9:
            print("%d * %d = %d" %(i, j, i * j))
            j += 1
        print()
        i += 1

def Cal(x):
    p = 1
    while p <= 9:
        print("%d * %d = %d" %(x, p, x * p))
        p += 1

In = int(input("Input a number : "))

if In == 0:
    Cal_Zero()

else:
    Cal(In)