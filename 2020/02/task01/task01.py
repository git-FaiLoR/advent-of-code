inputFile = open("input.txt", "r")
lineList = []
result = 0
counter = 0

for line in inputFile:
    strippedLine = line.strip()
    splitLine = strippedLine.split()
    lineList.append(splitLine)

for list in lineList:
    for part in list:
        counter = counter + 1
        if counter == 1:
            amount = (part.replace("-", " ").split())
            minimum = int(amount[0])
            maximum = int(amount[1])
        elif counter == 2:
            letter = part.strip(":")
        elif counter == 3:
            print(part.count(letter))
            if minimum <= part.count(letter) <= maximum:
                result = result + 1
            counter = 0

print(result)
