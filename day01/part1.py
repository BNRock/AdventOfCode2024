file = open("input.txt")
leftList = []
data = []
rightList = []
dif = 0
sum = 0

for line in (file.read().split("\n")):
    leftList.append(int(line.split()[0]))
    rightList.append(int(line.split()[1]))

for i in range(len(leftList)):
    dif = abs(min(leftList)-min(rightList))
    leftList.remove(min(leftList))
    rightList.remove(min(rightList))
    sum += dif

print(sum)