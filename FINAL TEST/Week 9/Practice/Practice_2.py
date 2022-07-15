def gcd(a,b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b

    global gcd
    gcd = a

    print("두 수의 최대 공약수는 %d입니다." %gcd)

def lcm(a,b):
    print("두 수의 최소 공배수는 %d입니다." %(a*b/gcd))

a = int(input("첫 번째 수를 입력하세요: "))
b = int(input("두 번째 수를 입력하세요: "))

gcd(a,b)
lcm(a,b)