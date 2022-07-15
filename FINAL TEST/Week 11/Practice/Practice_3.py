In = input("Input : ").split()

i = 0
list = ["A", "An", "The", "a", "an", "the"]

while i < len(In):
    if In[i] in list:
        del In[i]
    i += 1

print(In)