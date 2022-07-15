while True:
    n = input("숫자 하나를 입력하세요: ")
    if n.upper() == "E":
        print("종료합니다")
        break
    n = int(n)

    printStr = "%d = " % n
    divisor = 2

    while True:

        i = 0

        while n % divisor == 0:
            n //= divisor
            i += 1

        if i > 0: 
            printStr += "%d" % divisor
            if i > 1: printStr += "**%d" % i
            if n == 1: break
            printStr += " * "
        
        divisor += 1
        
    print(printStr)
    print()