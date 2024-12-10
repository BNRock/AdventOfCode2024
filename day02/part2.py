file = open("input.txt")
data = []
safe = 0
sum = 0

def ascendCheck(report):
    return report == sorted(report)

def descendCheck(report):
    return report == sorted(report, reverse=True)

def difCheck(report):
    for i in range(len(report)-1):
            dif = abs(report[i] - report[i+1])
            if dif < 1 or dif > 3:
                return False
            
    return True

def check(report):
     if (ascendCheck(report) or descendCheck(report)) and difCheck(report):
          return True
     return False

def removeElementRecheck(report):
    for i in range(len(report)):
        reportRemoved = list(report)
        reportRemoved.pop(i)
        print(reportRemoved)
        if(check(reportRemoved)):
            return True
        
    return False  
     
for line in (file.read().split("\n")):
    report = [int(item) for item in line.split()]
    if(check(report)):
        sum += 1
    else:
        sum += removeElementRecheck(report)
        
         
print(sum)

