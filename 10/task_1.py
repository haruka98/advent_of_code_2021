input = []
with open("input.txt") as file:
    input = file.readlines()

score = 0
for line in input:
    # (), [], {}, <>
    brackets = [0] * 4
    line_buildup = []
    for i in line:
        if i == "(" or i == "[" or i == "{" or i == "<":
            line_buildup += i
        elif (len(line_buildup) > 0 and (
              i == ")" and line_buildup[len(line_buildup) - 1] == "(" or
              i == "]" and line_buildup[len(line_buildup) - 1] == "[" or
              i == "}" and line_buildup[len(line_buildup) - 1] == "{" or
              i == ">" and line_buildup[len(line_buildup) - 1] == "<")):
            line_buildup.pop()
        else:
            if i == ")":
                score += 3
            if i == "]":
                score += 57
            if i == "}":
                score += 1197
            if i == ">":
                score += 25137
            break

print(score)
