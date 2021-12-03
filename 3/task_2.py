input = []
with open("input.txt") as file:
    input = file.readlines()

og_list = input
cs_list = input

ogr = 0
csr = 0

for i in range(0, 12):
    og_counter = 0
    og_new_list = []
    for line in og_list:
        og_counter += int(line[i])
    if og_counter >= len(og_list) / 2:
        for line in og_list:
            if line[i] == '1':
                og_new_list.append(line)
    else:
        for line in og_list:
            if line[i] == '0':
                og_new_list.append(line)
    og_list = og_new_list
    if len(og_list) == 1:
        ogr = int(og_list[0], 2)

    cs_counter = 0
    cs_new_list = []
    for line in cs_list:
        cs_counter += int(line[i])
    if cs_counter < len(cs_list) / 2:
        for line in cs_list:
            if line[i] == '1':
                cs_new_list.append(line)
    else:
        for line in cs_list:
            if line[i] == '0':
                cs_new_list.append(line)
    cs_list = cs_new_list
    if len(cs_list) == 1:
        csr = int(cs_list[0], 2)

print("Support rating:", ogr * csr)
