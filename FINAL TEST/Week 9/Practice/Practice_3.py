import random as r

num = r.randint(2, 100)

def FindNum(n):
    if n % 2 == 0:
        print("짝수는 소수가 아닙니다.")

    else:
        for i in range(3, n, 2):
            if n % i == 0:
                print("%d는 합성수입니다." %n)
                break
        else:
            print("%d는 소수입니다." %n)

FindNum(num)