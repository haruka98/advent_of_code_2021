# read file as two dimensional array
global input
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

# function to get the size of a basin recursively
def check_basin(i, j):
    if i < 0 or i >= len(input) or j < 0 or j >= len(input[i]) or input[i][j] == 9:
        return 0
    # mark position as done
    input[i][j] = 9
    # recursively check neighbour positions
    return 1 + check_basin(i - 1, j) + check_basin(i + 1, j) + check_basin(i, j - 1) + check_basin(i, j + 1)

# get all low points and get their basin size
global basin_list
basin_list = []
for i in range(len(input)):
    for j in range(len(input[i])):
        if is_low(i, j):
            basin_list.append(check_basin(i, j))

# multiply the three largest basins
counter = max(basin_list)
for i in range(2):
    basin_list.remove(max(basin_list))
    counter *= max(basin_list)

# output result
print("The product of the three largest basins is", counter)
