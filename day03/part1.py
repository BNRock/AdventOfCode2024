import re

file = open("input.txt")
sum = 0

for line in (file.read().split('\n')):
    mulList1 = re.findall(r'mul[(][0-9]+,[0-9]+[)]',line)
    for set in mulList1:
        numList = re.findall(r'[0-9]+', set)
        sum += int(numList[0])*int(numList[1])

print(sum)