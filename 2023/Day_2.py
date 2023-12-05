from aocd import get_data, submit
import math

data = get_data(day=2, year=2023).splitlines()

possibleConfig = ["12 red", "13 green", "14 blue"]

def Part1():
    ids, cubes = extractData()
    winners = []
    for id in ids:
        badID = False
        for round in cubes[id-1]:
            for color in round:
                if "red" in color:
                    if int(color[:2]) > 12 and color[1] != " ":
                        badID = True
                if "green" in color:
                    if int(color[:2]) > 13 and color[1] != " ":
                        badID = True
                if "blue" in color:
                    if int(color[:2]) > 14 and color[1] != " ":
                        badID = True
        if not badID:
            winners.append(id)
    
    return sum(winners)

def extractData():
    gameIdCounter = 0
    ids = []
    cubes = []
    for line in data:
        gameIdCounter += 1
        ids.append(gameIdCounter)
        cleanedLine = line.split(": ")[1]
        cleanedLine = cleanedLine.split("; ")
        fullySeperated = [segment.split(", ") for segment in cleanedLine]
        sortToRGB(fullySeperated)
        cubes.append(fullySeperated)
    return ids, cubes

def sortToRGB(fullySeperated):
    for segment in range(len(fullySeperated)):
        sorted = ["blank", "blank", "blank"]
        for part in fullySeperated[segment]:
            if "red" in part:
                sorted[0] = part
            elif "green" in part:
                sorted[1] = part
            elif "blue" in part:
                sorted[2] = part
        fullySeperated[segment] = sorted

def Part2():
    ids, cubes = extractData()
    powers = []
    for id in ids:
        redMax = -1
        greenMax = -1
        blueMax = -1
        for round in cubes[id-1]:
            for color in round:
                if "red" in color:
                    redNum = 0
                    if color[1] == " ":
                        redNum = int(color[0])
                    else:
                        redNum = int(color[:2])
                    if redMax < redNum:
                        redMax = redNum                        
                if "green" in color:
                    greenNum = 0
                    if color[1] == " ":
                        greenNum = int(color[0])
                    else:
                        greenNum = int(color[:2])
                    if greenMax < greenNum:
                        greenMax = greenNum
                if "blue" in color:
                    blueNum = 0
                    if color[1] == " ":
                        blueNum = int(color[0])
                    else:
                        blueNum = int(color[:2])
                    if blueMax < blueNum:
                        blueMax = blueNum
        powers.append(abs(redMax) * abs(greenMax) * abs(blueMax))
    return sum(powers)

print(f"Part 1: {Part1()}, Part 2: {Part2()}")
# submit(Part1(), day=2, year=2023)
# submit(Part2(), day=2, year=2023)