input = []
with open("input.txt") as file:
    input = [int(x) for x in file.readlines()]

current = 0
counter = -1
for line in input:
    if current < line:
        counter+=1
    current = line

print(counter)
