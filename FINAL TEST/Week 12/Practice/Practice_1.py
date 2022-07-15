In = input("In : ").split()

count = 0

for i in range(0, len(In)):
    if In[i][-1] == "동":
        print(In[i])
        count += 1

if count == 0:
    print("동이름이 없습니다.")