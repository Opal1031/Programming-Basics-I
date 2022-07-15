while True:

    a = int(input("첫 번째 수를 입력하세요: "))
    b = int(input("두 번째 수를 입력하세요: "))

    if a < b:
        a, b = b, a

    while b:
        a, b = b, a % b

    print("두 수의 최대 공약수는 %d입니다.\n" % a)