input_file = open("input.txt", "r")
line_list = []
result = 0
counter = 0

def logical_xor(string, position_1, position_2, letter, result):
    temp = list(string)
    if temp[position_1] == letter:
        if temp[position_2] != letter:
            result = result + 1
    elif temp[position_1] != letter:
        if temp[position_2] == letter:
            result = result + 1
    return result


for line in input_file:
    strippedLine = line.strip()
    splitLine = strippedLine.split()
    line_list.append(splitLine)

for list_line in line_list:
    for part in list_line:
        counter = counter + 1
        if counter == 1:
            amount = (part.replace("-", " ").split())
            position_1 = int(amount[0]) - 1
            position_2 = int(amount[1]) - 1
        elif counter == 2:
            letter = part.strip(":")
        elif counter == 3:
            result = logical_xor(part, position_1, position_2, letter, result)
            counter = 0

print(result)
