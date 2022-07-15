import random

maxHit = random.randint(7, 12)

while maxHit > 0:
    input("나무 내구력 : "+str(maxHit) + " -> HIT!! ")
    r = random.randint(1, 10)

    if r == 1:
        print("도끼를 놓쳤습니다.")
        break
    elif r == 2:
        print("크리티컬!!")
        maxHit -= 3
    else:
        maxHit -= 1

else:
    print("나무가 넘어갔습니다.")