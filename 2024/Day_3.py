from aocd import get_data, submit
import re
import sys
sys.path.append("../")
from Session import getSessionId

session_id = getSessionId()

data = get_data(session=session_id, day=3, year=2024)
data = "do()" + data + "don't()"

def Part1(data = data):
    sum = 0
    valid_muls = re.findall(r"mul\(\d+,\d+\)", data)
    for mul in valid_muls:
        numbers = str(mul).split("(")[1].strip(")")
        left, right = numbers.split(",")
        sum += int(left) * int(right)
    return sum

def Part2():
    return Part1("".join(re.findall(r"do\(\).*?don't\(\)", ("".join(data)).strip("\n"), flags=re.DOTALL)))

print(f"Part 1: {Part1()}, Part 2: {Part2()}")
# submit(Part1(), session=session_id, day=3, year=2024)
# submit(Part2(), session=session_id, day=3, year=2024)