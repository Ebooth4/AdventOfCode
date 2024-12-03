import sys
sys.path.append("../")
from Session import getSessionId
from aocd import get_data, submit

session_id = getSessionId()

data = get_data(session=session_id, day=1, year=2024).splitlines()

def Part1():
    return 0

def Part2():
    return 0

print(f"Part 1: {Part1()}, Part 2: {Part2()}")
# submit(Part1(), session=session_id, day=1, year=2024)
# submit(Part2(), session=session_id, day=1, year=2024)