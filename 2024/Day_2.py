import sys
sys.path.append("../")
from Session import getSessionId
from aocd import get_data, submit

session_id = getSessionId()

data = get_data(session=session_id, day=2, year=2024).splitlines()

def Part1():
    # numbers = []
    
    # result = 0
    # for line in data:
    #     safe = True
    #     numbers = list(map(int, line.split()))
        
    #     # print(numbers)
    #     if numbers[0] < numbers[1]:
    #         # Increasing
    #         for i in range(len(numbers)):
    #             if i != len(numbers) - 1:
    #                 if numbers[i] >= numbers[i+1]:
    #                     # print("Direction Change!")
    #                     safe = False
    #                     break
                    
    #                 if abs(numbers[i+1] - numbers[i]) > 3:
    #                     # print("Big Step!")
    #                     safe = False
    #                     break
                
    #     else:
    #         # Decreasing
    #         for i in range(len(numbers)):
    #             if i != len(numbers) - 1:
    #                 if numbers[i] <= numbers[i+1]:
    #                     # print("Direction Change!")
    #                     safe = False
    #                     break
                    
    #                 if abs(numbers[i+1] - numbers[i]) > 3:
    #                     # print("Big Step!")
    #                     safe = False
    #                     break
    #     # print("Safe? - " + str(safe))
    #     if safe:
    #         result += 1
    # return result
    return 0

def test(numbers, remove):
    del numbers[remove]
    i = 0
    safe = True
    while i != len(numbers) - 1:
        increasing = (numbers[0] <= numbers[1])
        print(str(numbers[i]) + " : " + str(numbers[i+1]))
        
        if numbers[i] >= numbers[i+1] and increasing:
            print("Direction Change!")
            safe = False
            break
        elif numbers[i] <= numbers[i+1] and not increasing:
            print("Direction Change!")
            safe = False
            break
        
        if abs(numbers[i+1] - numbers[i]) > 3:
            print("Big Step!")
            safe = False
            break
        i += 1
    print(safe)
    return safe

def Part2():
    numbers = []
    
    result = 0
    for line in data:
        dampened = 0
        safe = False
        numbers = list(map(int, line.split()))
        i = 0
        print(numbers)
        for i in range(len(numbers)):
            if test(numbers.copy(), i):
                safe = True
                break
    
        print("Safe? - " + str(safe))
        if safe:
            result += 1
    return result

print(f"Part 1: {Part1()}, Part 2: {Part2()}")
# submit(Part1(), session=session_id, day=2, year=2024)
# submit(Part2(), session=session_id, day=2, year=2024)