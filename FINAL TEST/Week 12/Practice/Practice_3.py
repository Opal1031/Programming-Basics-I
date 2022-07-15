import random as r

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

secret = r.sample(num, 3)
secret.sort()

for i in range(0, 10):
    guess = input("\n세 개의 숫자를 입력하세요 : ").split(", ")

    strike = 0
    ball = 0

    for p in range(0, 3):
        for q in range(0, 3):
            if secret[p] == guess[q]:
                if p == q:
                    strike += 1
                else:
                    ball += 1

    if strike == 0 and ball == 0:
        print("OUT!!")
    elif strike == 3:
        print("정답입니다.")
        break
    else:
        print("%d STRIKE %d BALL" %(strike, ball))

    print("기회가 %d번 남았습니다." %(9 - i))

print("\n정답은 ", secret , "입니다.")