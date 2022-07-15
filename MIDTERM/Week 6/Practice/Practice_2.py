size = int(input("나무 크기 : "))
leaf = input("잎 모양 : ")
stem = input("줄기 모양 : ")

n = 1
i = 1

while n <= size:
    print(" " * (size-n) + leaf * n)
    n += 1

while i <= (size//2):
    print(" " * (size-1) + stem)
    i += 1