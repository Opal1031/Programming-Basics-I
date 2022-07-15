while True:
    n = input("숫자 하나를 입력하세요: ")

    if n.upper() == "E":
        print("종료합니다")
        break

    n = int(n)
    sum = 0
    step = 1

    i = step
    
    while i <= n:
        sum += i
        i += step
        
    print("1부터 %d까지의 합은 %d입니다.\n" % (n, sum))