# read file as two dimensional array
input = []
with open("input.txt") as file:
    input = [[int(x) for x in line.strip()] for line in file.readlines()]

# total amount of flashes
flashes = 0

# function to check for flash and trigger surrounding
def flash(i, j):
    if input[i][j] > 9:
        global flashes
        flashes += 1
        input[i][j] = -999
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if not (x == i and y == j):
                    if x in range(len(input)) and y in range(len(input[i])):
                        input[x][y] += 1
                        flash(x, y)

# function to make one step
def step():
    # increase energy level of all by 1
    for i in range(len(input)):
        for j in range(len(input[i])):
            input[i][j] += 1
    # check for flashes
    for i in range(len(input)):
        for j in range(len(input[i])):
            flash(i, j)
    # set all that flashed to 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] < 0:
                input[i][j] = 0

# 100 steps
for i in range(100):
    step()

# output result
print(flashes)
