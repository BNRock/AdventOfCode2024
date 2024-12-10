def diagSearch(arr, row, col):
    sum = 0
    letList = []
    try:
        letList.extend([arr[row-1][col-1], arr[row+1][col+1], arr[row-1][col+1], arr[row+1][col-1]])
        
        if(letList.count('M') == 2 and letList.count('S') == 2):
            if(arr[row-1][col-1] != arr[row+1][col+1]):
                sum += 1
    except IndexError:
        pass
    return sum

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
        if(search[x][y] == 'A'):
            sum += diagSearch(search,x,y)
            
            
            
print(sum)