def horizSearch(arr, row, col):
    sum = 0
    try:
        if(arr[row][col+1] == 'M') and (arr[row][col+2] == 'A') and (arr[row][col+3] == 'S'):
            sum +=1
    except IndexError:
        pass
    
    try:
        if (arr[row][col-1] == 'M') and (arr[row][col-2] == 'A') and (arr[row][col-3] == 'S'):
            sum += 1
    except IndexError:
        pass
    return sum

def vertSearch(arr, row, col):
    sum = 0
    try:
        if(arr[row+1][col] == 'M') and (arr[row+2][col] == 'A') and (arr[row+3][col] == 'S'):
            sum += 1
    except IndexError:
        pass
    
    try:
        if (arr[row-1][col] == 'M') and (arr[row-2][col] == 'A') and (arr[row-3][col] == 'S'):
            sum +=1
    except IndexError:
        pass
    return sum

def diagSearch(arr, row, col):
    sum = 0
    try:
        if(arr[row-1][col+1] == 'M') and (arr[row-2][col+2] == 'A') and (arr[row-3][col+3] == 'S'):
            sum += 1
    except IndexError:
        pass
    
    try:
        if (arr[row+1][col-1] == 'M') and (arr[row+2][col-2] == 'A') and (arr[row+3][col-3] == 'S'):
            sum += 1
    except IndexError:
        pass
    
    try:
        if(arr[row+1][col+1] == 'M') and (arr[row+2][col+2] == 'A') and (arr[row+3][col+3] == 'S'):
            sum += 1
    except IndexError:
        pass
    
    try:
        if (arr[row-1][col-1] == 'M') and (arr[row-2][col-2] == 'A') and (arr[row-3][col-3] == 'S'):
            sum += 1
    except IndexError:
        pass
    return sum

def searchAll(search, row, col):
    return horizSearch(search, row, col) + vertSearch(search, row, col) + diagSearch(search, row, col)


search = []
letters = []
sum = 0

file = open("input.txt")
for line in (file.read().split('\n')):
    line = "...." + line + "...."
    for letter in line:
        letters.append(letter)
    search.append(list(letters))
    letters.clear()

for i in range(4): search.insert(0, "."*len(search[0]))
for i in range(4): search.append("."*len(search[0]))

for x, row in enumerate(search):
    for y, col in enumerate(row):
        if(search[x][y] == 'X'):
            sum += searchAll(search, x, y)
            
            
            
print(sum)
    
    


