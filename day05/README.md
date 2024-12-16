## Soln
# Part 1
- For each first number before the brace, add the first number as the key to a dict, then add the second numbre to a list for the key's value.

- Then make a list of each print order
- For each print order element:
    - access the list (value) of the element (key)
    - for each element in order list: if elem (x in x|y) is in print order: if print order index is greater than current index of y(y in x|y), then this means that x is coming after y, which is a violation so order is not correct.

- IF CORRECT print order, add middle number to sum

# Part 2
- For each incorrect order, go through each element in order list
    - for each element in order list, check if out of order according to dictionary
    - for each violiation of order, swap the two elements
    - repeat until solved