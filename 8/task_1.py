# read file into input
input = []
with open("input.txt") as file:
    input = file.read().splitlines()

# count 1, 4, 7 and 8
counter = 0
for line in input:
    output_numbers = line.split(" | ")[1].split(" ")
    for i in range(len(output_numbers)):
        if len(output_numbers[i]) == 2 or len(output_numbers[i]) == 3 or len(output_numbers[i]) == 4 or len(output_numbers[i]) == 7:
            counter += 1

# print result
print(counter)
