money = int(input("자판기에 넣을 돈은? : "))
coke = int(input("콜라 개수는? : "))

re_money = money - 600 * coke

print("거스름돈은 %d원입니다." %re_money)
print("500원 동전은 %d개, 100원 동전은 %d개가 나왔습니다." %(re_money//500, (re_money%500)/100))