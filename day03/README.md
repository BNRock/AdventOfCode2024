## Soln
# Part 1
- search entire string for instances of mul(, then take input from there with regex to find number,comma,number, )
- then loop through each mul call, multiply numbers, add to sum

# Part 2
- Search for do() and don't() with regex, the set corresposding flag to true or false which dictates whether or not the mul is added to a sum

-either use [m.start() for m in re.finditer('do()', list)], to get list of indexes, OR
do a loop with string.find(do(), index), where index is the index of the last found do() + 1, So it just finds the next do() or don't() over and over
