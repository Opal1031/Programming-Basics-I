name = input("이름을 입력하세요 : ")
KOR = int(input("국어 점수 : "))
MATH = int(input("수학 점수 : "))
ENG = int(input("영어 점수 : "))

if (KOR + MATH + ENG) >= 180:
    if KOR >= 40 and MATH >= 40 and ENG >= 40:
        print("합격")
    else:
        print("과락")
else:
    print("불합격")