list = ["커피", "우유", "바나나", "감귤", "화장지", "장갑", "이불", "베개", "장난감", "음료수", "빵"]

while True:
    In = int(input("\n상품관리(1. 삽입, 2. 삭제, 3. 상품 확인, 4. 재고 확인) : "))

    if In == 1:
        a = input("\n상품관리1 - 삽입) 삽입하고자 하는 상품은? : ")
        b = int(input("\n상품관리1 - 삽입) 삽입하고자 하는 위치는? : "))
        list.insert(b, a)

    elif In == 2:
        c = input("\n상품관리2 - 삭제) 삭제하고자 하는 상품은? : ")
        list.remove(c)

    elif In == 3:
        d = input("\n상품관리3 - 상품 확인) 확인하고자 하는 상품은? : ")
        print(d in list)

    elif In == 4:
        print("\n상품관리4 - 재고확인 : ", list,"\n상품관리 프로그램은 종료합니다.")
        break

    else:
        print("\n상품관리를 위한 명령어가 아닙니다.\n다시 선택하십시오.")