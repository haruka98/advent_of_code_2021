input = []
with open("input.txt") as file:
    input = file.readlines()

columns = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for line in input:
    for i in range(0, 12):
        columns[i] += int(line[i])

gamma_rate = 0

for i in range(0, 12):
    if columns[i] > len(input) / 2:
        gamma_rate += pow(2, -1 * i + 11)

print("Power consumption:", gamma_rate * (pow(2, 12) - 1 - gamma_rate))
