import re

file = open("input.txt")
sum = 0
doFlag = 1
doIndex = 0
dontIndex = 0
mulIndex = 0
rangeList = []

def findClosestPrev(targetIdx, doList, dontList, max):
    doDifDict = {}
    dontDifDict = {}
    for do in doList: 
        if do <= targetIdx:
            doDifDict.update({do:targetIdx-do}) #key is do index in string, value is length between do index and mul call
    
    print("DODICT: ", doDifDict)     
    for dont in dontList:
        if dont <= targetIdx:
            dontDifDict.update({dont:targetIdx-dont})
            
    print("DONTDICT: ", dontDifDict)    
    minDo = min(doDifDict.values(), default = max)
    minDont = min(dontDifDict.values(), default=max)
    
    #return 0 for dont flag, 1 for do flag
    print("DO?: ", minDo < minDont)
    return minDo < minDont


for line in (file.read().split('\n')):
    print(line)
    dontList = [m.start() for m in re.finditer('don\'t\(\)', line)]
    doList = [m.start() for m in re.finditer('do\(\)', line)]
    if doFlag: doList.insert(0, 0)
    print("DO: ", doList, " DONT: ", dontList)
    #dontList.append(len(line))
    #dontIndex = line.find("don't()", dontIndex)
    '''for i in range(len(doList)):
        rng = range(doList[i], dontList[i])
        rangeList.append(rng)
        print("I: ", i)
    '''    
    print("RANGELIST:", rangeList)
   
    mulList1 = re.findall(r'mul[(][0-9]+,[0-9]+[)]',line)
    for set in mulList1:
        mulIndex = line.find(set)
        print("MULDEX: ", mulIndex, "CALL: ", set)
        #Multiply numbers if the index of the mul is between do and dont ()
        #for rngElem in rangeList:
        
        if findClosestPrev(mulIndex, doList, dontList, len(line)):
            #print("MUL INDEX ", mulIndex, " IN RANGE: ", rngElem)
            numList = re.findall(r'[0-9]+', set)
            sum += int(numList[0])*int(numList[1])
            print("ADDED\n")
                
    #dontIndex += 1
    #doIndex += 1
    #doIndex = line.find("do()", doIndex)
    try:
        doFlag = 0 if dontList[-1] > doList[-1] else 1
    except IndexError:
        pass
print(sum)