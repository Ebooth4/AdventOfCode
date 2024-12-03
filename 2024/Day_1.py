import sys
sys.path.append("../")
from Session import getSessionId
from aocd import get_data, submit

session_id = getSessionId()

data = get_data(session=session_id, day=1, year=2024).splitlines()
left = []
right = []
for line in data:
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))

def Part1():
    total_difference = 0
    left.sort()
    right.sort()
    for i in range(len(left)):
        total_difference += abs(left[i] - right[i])
    return total_difference

def Part2():
    similarity_score = 0
    for i in range(len(left)):
        occurances = right.count(left[i])
        similarity_score += (left[i] * occurances)
    return similarity_score

print(f"Part 1: {Part1()}, Part 2: {Part2()}")
# submit(Part1(), session=session_id, day=1, year=2024)
submit(Part2(), session=session_id, day=1, year=2023)