num = int(input("Input a number : "))
i = 1
k = 2

if num == 0:
    while k <= 9:
        while i <= 9:
            print("%d * %d = %d" %(k, i, k*i))
            i += 1
        k += 1
        i = 1

else:
    while i < 10:
        print("%d * %d = %d" %(num, i, num*i))
        i += 1