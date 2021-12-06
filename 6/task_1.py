fishes = []
with open("input.txt") as file:
    fishes = [int(x) for x in file.readline().split(",")]

# daily update fish population
def one_day(fishes):
    new_fish = 0
    for i in range(len(fishes)):
        if fishes[i] == 0:
            new_fish += 1
            fishes[i] = 6
        else:
            fishes[i] -= 1
    for j in range(new_fish):
        fishes.append(8)
    return fishes

# wait 80 days
for i in range(80):
    fishes = one_day(fishes)

print(len(fishes))
