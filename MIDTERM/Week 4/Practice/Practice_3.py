weight = input("체중을 입력하세요(kg) : ")
height = input("신장을 입력하세요(cm) : ")
print()
BMI = float(weight) / (float(height)/100)**2
print("BMI는 %.2f" %BMI, "입니다.")