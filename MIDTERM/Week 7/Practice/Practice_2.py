import random

secret = random.randint(1,50)
chance = 5

while chance > 0:
    guess = int(input("병 뚜껑에 적힌 숫자를 맞춰보세요 : "))

    if secret > guess:
        print("high")
    elif secret < guess:
        print("low")
    else:
        break
    
    chance -= 1

if chance == 0:
    print("병 뚜껑에 적힌 숫자 : %d" %secret)

if guess == secret:
    print("숫자를 맞췄습니다.")