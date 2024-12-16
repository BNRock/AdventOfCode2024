import math

file = open("input.txt")
spaceFlag = 0
sum = 0
rulesDict = {}
printerList = []
printOrder = []

def orderCheck(printOrder, rulesDict):
    for page in printOrder:
        pageRules = rulesDict.get(page, [])
        for order in pageRules:
            if order in printOrder:
                if printOrder.index(order) < printOrder.index(page):
                    return False
    return True

def reOrder(printOrder, rulesDict):
    for page in printOrder:
        pageRules = rulesDict.get(page, [])
        for order in pageRules:
            if order in printOrder:
                if printOrder.index(order) < printOrder.index(page):
                    in1 = printOrder.index(order)
                    in2 = printOrder.index(page)
                    printOrder[in1], printOrder[in2] = printOrder[in2], printOrder[in1]
                    
                    if not orderCheck(printOrder,rulesDict):
                        reOrder(printOrder, rulesDict)
    
    return int(printOrder[math.floor(len(printOrder)/2)])


for line in (file.read().strip().split('\n')):
    if (line in '\n'): 
        spaceFlag = 1
        continue
    
    if(not spaceFlag):
        lineSplit = line.split("|")
        if (lineSplit[0] in rulesDict.keys()):
           rulesDict.get(lineSplit[0]).append(lineSplit[1]) # Add y in x|y to the list in the dictionary at key x
        else: 
            rulesDict[lineSplit[0]] = [lineSplit[1]]
    else:
        printOrder = line.split(",")
        printerList.append(printOrder)
        if(not orderCheck(printOrder, rulesDict)):
            sum += reOrder(printOrder, rulesDict)
        
print(sum)