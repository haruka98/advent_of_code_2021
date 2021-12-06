# read input as list of pairs with (age, amount)
fishes = []
with open("input.txt") as file:
    for x in file.readline().split(","):
        pair = (int(x), 1)
        fishes.append(pair)

# daily update fish population
def one_day(fishes):
    new_fish = 0
    for i in range(len(fishes)):
        if fishes[i][0] == 0:
            new_fish += fishes[i][1]
            fishes[i] = (6, fishes[i][1])
        else:
            fishes[i] = (fishes[i][0] - 1, fishes[i][1])
    fishes.append((8, new_fish))
    return fishes

# wait 256 days
for i in range(256):
    fishes = one_day(fishes)

# sum up all fish
sum = 0
for i in range(len(fishes)):
    sum += fishes[i][1]

print(sum)
