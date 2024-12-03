from aocd import get_data, submit
import re

session_id = "53616c7465645f5f6bfb145c34ba6da6e83b6bdff57e16a58c51162017789dc8894da75aefa5d050c9f8f3642364df1e5e6acd719107a90d70e686cac7317033"

data = get_data(session=session_id, day=3, year=2024)
data = "do()" + str(data) + "don't()"

testing_file = open("test.txt")
test_data = testing_file.read()


def Part1():
    sum = 0
    valid_muls = re.findall(r"mul\(\d+,\d+\)", data)
    for mul in valid_muls:
        numbers = str(mul).split("(")[1].strip(")")
        left, right = numbers.split(",")
        sum += int(left) * int(right)
    return sum

def Part2():
    # BROKEN, My Regex doesn't work for some reason
    # Got the answer by using VSCodes regexto format .txt file and ran normal part1 stuff of formatted input data
    sum = 0
    # do_and_donts = re.findall(r"do\(\).*?don't\(\)", data.strip("\n"))
    # print(len(do_and_donts))
        
    valid_muls = re.findall(r"mul\(\d+,\d+\)", "".join(test_data.strip("\n")))
    for mul in valid_muls:
        numbers = str(mul).split("(")[1].strip(")")
        left, right = numbers.split(",")
        sum += int(left) * int(right)
    return sum

print(f"Part 1: {Part1()}, Part 2: {Part2()}")
# submit(Part1(), session=session_id, day=3, year=2024)
# submit(Part2(), session=session_id, day=3, year=2024)