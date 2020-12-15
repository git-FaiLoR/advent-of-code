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
                for third in range(len(inputArray)):
                    if tempNumber != inputArray[third] and inputArray[second] != inputArray[third]:
                        if tempNumber + inputArray[second] + inputArray[third] == 2020:
                            solution = tempNumber * inputArray[second] * inputArray[third]
                            controlBoolean = "false"

print(solution)