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

def tree_calculation(list_of_lists, position_1, position_2, result, pos_1_increment, pos_2_increment):
    while position_1 < len(list_of_lists):
        if position_2 >= len(list_of_lists[0]):
            position_2 -= len(list_of_lists[0])
        if list_of_lists[position_1][position_2] == "#":
            result += 1
        position_1 += pos_1_increment
        position_2 += pos_2_increment
    return result

result = tree_calculation(list_of_lists, position_1, position_2, 0, 1, 1)
result *= tree_calculation(list_of_lists, position_1, position_2, 0, 1, 3)
result *= tree_calculation(list_of_lists, position_1, position_2, 0, 1, 5)
result *= tree_calculation(list_of_lists, position_1, position_2, 0, 1, 7)
result *= tree_calculation(list_of_lists, position_1, position_2, 0, 2, 1)

print(result)
