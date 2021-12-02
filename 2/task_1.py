input = []
with open("input.txt") as file:
    input = file.readlines()

horizontal_position = 0
depth = 0

for entry in input:
    array = entry.split()
    if array[0] == "forward":
        horizontal_position += int(array[1])
    if array[0] == "down":
        depth += int(array[1])
    if array[0] == "up":
        depth -= int(array[1])

print("horizontal position:", horizontal_position)
print("depth:", depth)
print("total:", horizontal_position * depth)
