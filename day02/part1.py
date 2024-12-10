file = open("input.txt")
data = []
safe = 0
sum = 0

for line in (file.read().split("\n")):
    report = [int(item) for item in line.split()]
    if report == sorted(report) or report == sorted(report, reverse=True): #If list is ascending or descending
        safe = 1
        for i in range(len(report)-1):
            dif = abs(report[i] - report[i+1])
            if dif < 1 or dif > 3:
                safe = 0        
    sum += safe
    safe = 0

print(sum)