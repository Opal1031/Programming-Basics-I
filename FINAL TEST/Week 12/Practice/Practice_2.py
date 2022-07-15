import random as r

Num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
money = 0

while True:
    Lucky = r.sample(Num, 4)
    Lucky.sort()

    print("\n복권 번호를 맞춰보세요~")
    Guess = input("\n네 개의 숫자를 입력하세요 : ").split()
    Guess.sort()

    x = 0
    for y in range(0, 4):
        for z in range(0, 4):
            if Lucky[y] == Guess[z]:
                x += 1

    win = x * 2500
    print("\n%d개를 맞춰 당첨금은 %d원입니다." %(x, win))
    money += win

    print("누적 당첨금은 %d원입니다." %money)
    re = input("\n한번 더 하시겠습니까? : ")
    if re.upper() == "N":
        print("\n프로그램을 종료합니다.")
        break

print("\n총 당첨금은 %d원입니다." %money)