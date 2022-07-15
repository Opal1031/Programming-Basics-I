salt = int(input("소금의 양은? : "))
water = int(input("물의 양은? : "))

mix = (salt/(salt+water)) * 100

print("소금물의 농도는 %.3f%%입니다." %mix)