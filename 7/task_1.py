# read input as list of int
input = []
with open("input.txt") as file:
    input = [int(x) for x in file.readline().split(",")]

# calculate fuel for every position
fuel = [0] * max(input)
for i in range(max(input)):
    for j in range(len(input)):
        fuel[i] += abs(input[j] - i)

# print position and minimum required fuel
print("The best position is", fuel.index(min(fuel)), "and requires", min(fuel), "fuel.")
