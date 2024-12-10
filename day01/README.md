- two list, aligned vertically
- pair smallet number in left list with smallest number in right list, 2nd smallest num in left with 2nd smallest right, eetc.

- within each pair, find the difference between each pair, then sum all of them

## soln:
- read input, sort each list into array
- for loop:
    - in each array, take absolute val of difference between min number, add to counter sum, then remove from array
    - return sum


# part two:
- loop thru left list, count how many times each number is in right list, add product to sum

