input = []
with open("input.txt") as file:
    input = file.readlines()

total_score = []
for line in input:
    score = 0
    # (), [], {}, <>
    brackets = [0] * 4
    line_buildup = []
    broken = False
    for i in line.strip():
        if i == "(" or i == "[" or i == "{" or i == "<":
            line_buildup += i
        elif (len(line_buildup) > 0 and (
              i == ")" and line_buildup[len(line_buildup) - 1] == "(" or
              i == "]" and line_buildup[len(line_buildup) - 1] == "[" or
              i == "}" and line_buildup[len(line_buildup) - 1] == "{" or
              i == ">" and line_buildup[len(line_buildup) - 1] == "<")):
            line_buildup.pop()
        else:
            broken = True
            break
    if not broken:
        line_buildup.reverse()
        for i in line_buildup:
            score *= 5
            if i == "(":
                score += 1
            if i == "[":
                score += 2
            if i == "{":
                score += 3
            if i == "<":
                score += 4
        total_score += [score]

print(sorted(total_score)[int(len(total_score) / 2)])
