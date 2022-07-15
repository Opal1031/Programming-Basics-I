money = int(input("동전을 넣으세요 : "))

if money > 500:
    print("콜라가 %d 개 나왔습니다." %(money//500))
    print("거스름돈 %d 원이 나왔습니다." %(money%500))