drinks = ["콜라", "사이다", "환타"]
coin = int(input("동전을 넣으세요 : "))

while coin >= 500:
    print("\n현재 금액 : ", coin, "원")
    sel = int(input("콜라(0), 사이다(1), 환타(2) : "))
    print(drinks[sel] + "가 나왔습니다.")
    coin -= 500

print("거스름돈 : ", coin, "원")