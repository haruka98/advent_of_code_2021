input = []
with open("input.txt") as file:
    input = [int(x) for x in file.readlines()]

numbers = []
for i in range(1, len(input) - 1):
    numbers.append(input[i - 1] + input[i] + input[i + 1])

current = -1
counter = -1
for entry in numbers:
    if current < entry:
        counter += 1
    current = entry

print(counter)
