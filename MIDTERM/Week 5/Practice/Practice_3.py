dust = int(input("오늘의 미세 먼지 농도는? : "))

if dust <= 30:
    print("오늘의 미세먼지는 좋음 입니다.")
elif dust <= 80:
    print("오늘의 미세먼지는 보통 입니다.")
elif dust <= 150:
    print("오늘의 미세먼지는 나쁨 입니다.")
else:
    print("오늘의 미세먼지는 매우 나쁨 입니다.")

if dust > 100:
    print("미세먼지 경계 단계입니다!!")