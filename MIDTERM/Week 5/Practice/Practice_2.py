age = int(input("당신의 나이는 몇 살입니까? : "))

if age < 18:
    family = input("동승자가 있습니까? : ")

    if family.upper() == "N":
        print("탑승할 수 없습니다...")

    print("감사합니다.")