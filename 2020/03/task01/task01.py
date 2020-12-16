input_file = open("input.txt", "r")
line_list = []
list_of_lists = []
position_1 = 0
position_2 = 0
result = 0

for line in input_file:
    line_list.append(line.strip("\n").split())

for element in line_list:
    list_of_lists.append(list(element[0]))

while position_1 < len(list_of_lists):
    if position_2 >= len(list_of_lists[0]):
        position_2 -= len(list_of_lists[0])
    if list_of_lists[position_1][position_2] == "#":
        result += 1
    print(list_of_lists[position_1][position_2])
    print(result)
    position_1 += 1
    position_2 += 3
