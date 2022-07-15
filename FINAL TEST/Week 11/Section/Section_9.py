inputScores = input("Input scores : ")
scores = inputScores.split()

sum = 0
index = 0

while index < len(scores):
    sum += int(scores[index])
    index += 1

print("Sum : ", sum)