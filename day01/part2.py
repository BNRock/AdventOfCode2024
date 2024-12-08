file = open("input.txt")
leftList = []
data = []
rightList = []
prod = 0
sum = 0

for line in (file.read().split("\n")):
    leftList.append(int(line.split()[0]))
    rightList.append(int(line.split()[1]))

numDict = {ct:rightList.count(ct) for ct in rightList} #Makes dictionary with leftListNum: Quantity of leftListNum

for num in leftList:
    prod = num*numDict.get(num, 0)
    sum += prod

print(sum)