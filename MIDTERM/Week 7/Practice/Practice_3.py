import random

coin = int(input("동전을 넣으세요 : "))

while coin >= 0:
    
    run = input("끝내시겠습니까? ")

    if run.upper() == 'Y':
        print("출력금액 %d" %coin)
        break

    else:
        if random.randint(1, 10) == 1:
            coin += 5000
            print("당첨(+5000)")

        else:
            coin -= 1000
            print("꽝!(-1000)")

        print("현재금액 : %d" %coin)