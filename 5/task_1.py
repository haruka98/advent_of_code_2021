import numpy as np
import re

# get input from file
input = []
with open("input.txt") as file:
    input = file.readlines()

# create initial array of zeros
array = np.zeros((1000, 1000))

# fill array with values
for line in input:
    # get line as list
    values = list(map(int, re.split(r",| -> ", line)))
    # test for horizontal or vertical
    if values[0] == values[2] or values[1] == values[3]:
        for i in range(min(values[0], values[2]), max(values[0], values[2]) + 1):
            for j in range(min(values[1], values[3]), max(values[1], values[3]) + 1):
                array[i][j] = int(array[i][j]) + 1

# count values greater 1
counter = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        if array[i][j] > 1:
            counter += 1

# output result
print(counter)
