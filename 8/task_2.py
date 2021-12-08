# read file into input
input = []
with open("input.txt") as file:
    input = file.read().splitlines()

# function to check whether all chars of a smaller string are included in a bigger string
def includes(bigger_string, smaller_string):
    for char in smaller_string:
        if char not in bigger_string:
            return False
    return True

# loop over each line
counter = 0
for line in input:
    input_numbers = line.split(" | ")[0].split(" ")
    true_numbers = [-1] * 10
    # get numbers by length of string
    for i in range(len(input_numbers)):
        if len(input_numbers[i]) == 2:
            true_numbers[i] = 1
        if len(input_numbers[i]) == 3:
            true_numbers[i] = 7
        if len(input_numbers[i]) == 4:
            true_numbers[i] = 4
        if len(input_numbers[i]) == 7:
            true_numbers[i] = 8
    # get numbers with length of 6 (6 is required later for numbers of length 5)
    for i in range(len(input_numbers)):
        if len(input_numbers[i]) == 6 and true_numbers[i] == -1:
            # 9 includes 4
            if includes(input_numbers[i], input_numbers[true_numbers.index(4)]):
                true_numbers[i] = 9
            # 0 includes 1
            elif includes(input_numbers[i], input_numbers[true_numbers.index(1)]):
                true_numbers[i] = 0
            else:
                true_numbers[i] = 6
    # get numbers with length of 5
    for i in range(len(input_numbers)):
        if len(input_numbers[i]) == 5 and true_numbers[i] == -1:
            # 3 includes 7
            if includes(input_numbers[i], input_numbers[true_numbers.index(7)]):
                true_numbers[i] = 3
            # 6 includes 5 (got 6 from above)
            elif includes(input_numbers[true_numbers.index(6)], input_numbers[i]):
                true_numbers[i] = 5
            else:
                true_numbers[i] = 2
    # translate all output numbers and add them to counter
    output_numbers = line.split(" | ")[1].split(" ")
    for i in range(4):
        for j in range(10):
            if sorted(output_numbers[i]) == sorted(input_numbers[j]):
                counter += pow(10, 3 - i) * true_numbers[j]

# print result
print(counter)
