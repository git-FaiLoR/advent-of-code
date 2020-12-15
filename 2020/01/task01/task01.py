inputArray = []
file = open("input.txt", "r")

for line in file:
    inputArray.append(int(line.strip()))

controlBoolean = "true"

while controlBoolean == "true":
    for first in range(len(inputArray)):
        tempNumber = inputArray[first]
        for second in range(len(inputArray)):
            if tempNumber != inputArray[second]:
                if tempNumber + inputArray[second] == 2020:
                    solution = tempNumber * inputArray[second]
                    controlBoolean = "false"

print(solution)