from aocd import get_data, submit

data = get_data(day=1, year=2023).splitlines()

def Part1():
    numList = []
    for line in data:
        numList += [char for char in line if char.isdigit()]
        numList += ["break"]
    return combineAndSumNumsPart1(numList)

def combineAndSumNumsPart1(numList):
    doubleDigitNums = []
    firstNum = -1
    lastNum = -1
    for element in numList:
        if element == "break" : 
            if lastNum == -1:
                lastNum = firstNum
            doubleDigitNums.append(int(str(firstNum) + str(lastNum)))
            firstNum = -1 
            lastNum = -1
            continue
        if firstNum == -1: firstNum = element
        else : lastNum = element

    return sum(doubleDigitNums)

def Part2():
    numList = []
    for line in data:
        offset = 0
        for char in line:
            if char.isdigit(): numList.append(char)
            else: textToNum(line, offset, numList)
            offset += 1
        numList += ["break"]
        print(line)
        print(numList[-8:])
    return combineAndSumNumsPart2(numList)

def textToNum(line, offset, numList):
    if line[offset] == 'o' and line[offset:offset+3] == "one" :
        numList.append('1')
    elif line[offset] == 't' and line[offset:offset+3] == "two" :
        numList.append('2')
    elif line[offset] == 't' and line[offset:offset+5] == "three" :
        numList.append('3')
    elif line[offset] == 'f' and line[offset:offset+4] == "four" :
        numList.append('4')
    elif line[offset] == 'f' and line[offset:offset+4] == "five" :
        numList.append('5')
    elif line[offset] == 's' and line[offset:offset+3] == "six" :
        numList.append('6')
    elif line[offset] == 's' and line[offset:offset+5] == "seven" :
        numList.append('7')
    elif line[offset] == 'e' and line[offset:offset+5] == "eight" :
        numList.append('8')
    elif line[offset] == 'n' and line[offset:offset+4] == "nine" :
        numList.append('9')        

def combineAndSumNumsPart2(numList):
    doubleDigitNums = []
    firstNum = -1
    lastNum = -1
    for element in numList:
        if element == "break" : 
            if lastNum == -1:
                lastNum = firstNum
            doubleDigitNums.append(int(str(firstNum) + str(lastNum)))
            firstNum = -1 
            lastNum = -1
            continue
        if firstNum == -1: firstNum = element
        else : lastNum = element
    print(doubleDigitNums)

    return sum(doubleDigitNums)

print(f"Part 1: {Part1()}, Part 2: {Part2()}")
# submit(Part1(), day=1, year=2023)
# submit(Part2(), day=1, year=2023)