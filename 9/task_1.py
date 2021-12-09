# read file as two dimensional array
input = []
with open("input.txt") as file:
    input = [[int(i) for i in line.strip()] for line in file.readlines()]

# function to check whether a point is a low point
def is_low(i, j):
    if(i > 0 and input[i - 1][j] <= input[i][j] or
       i < len(input) - 1 and input[i + 1][j] <= input[i][j] or
       j > 0 and input[i][j - 1] <= input[i][j] or
       j < len(input[i]) - 1 and input[i][j + 1] <= input[i][j]):
        return False
    return True

# calculate risk level by looping over the full array
risk_level = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        if is_low(i, j):
            risk_level += input[i][j] + 1

# print result
print("The risk level is at", risk_level)
