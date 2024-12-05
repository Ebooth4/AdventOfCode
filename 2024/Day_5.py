import sys
sys.path.append("../")
from Session import getSessionId
from aocd import get_data, submit
import networkx as nx

session_id = getSessionId()

data = get_data(session=session_id, day=5, year=2024).split("\n\n")
unformatted_rules = data[0].splitlines()
unformatted_updates = data[1].splitlines()
updates = []
rules = []
for update in unformatted_updates:
    updates.append(list(map(int, update.split(","))))
for rule in unformatted_rules:
    before, after = map(int, rule.split("|"))
    rules.append((before, after))


def check_sequence(rules: list[tuple[int, int]], updates: list[list]):
    valid = []
    invalid = []
    for update in updates:
        so_far_valid = True
        for before, after in rules:
            try:
                if update.index(before) > update.index(after):
                    so_far_valid = False
                    break
            except ValueError:
                continue
        if so_far_valid:
            valid.append(update)
        else:
            invalid.append(update)
    return valid, invalid

def Part1():
    valid, invalid = check_sequence(rules, updates)
    sum = 0
    for update in valid:
        sum += update[len(update) // 2]
    return sum

def create_graph(rules, update):
    graph = nx.DiGraph()
    for before, after in rules:
        if before in update and after in update:
            graph.add_edge(before, after)
            
    
    if not nx.is_directed_acyclic_graph(graph):
        raise ValueError("CYCLES!!!")
    
    sorted_sequence = list(nx.topological_sort(graph))
    return sorted_sequence

# def arrange(rules, invalid):
#     fixed = []
#     for update in invalid:
#         for before, after in rules:
#             try:
#                 if update.index(before) > update.index(after):
                    
                    
#             except ValueError:
#                 continue
#     return fixed

def Part2():
    valid, invalid = check_sequence(rules, updates)
    sum = 0
    for update in invalid:
        sorted_sequence = create_graph(rules, update)
        sum += sorted_sequence[len(sorted_sequence) // 2]

    return sum

print(f"Part 1: {Part1()}, Part 2: {Part2()}")
# submit(Part1(), session=session_id, day=5, year=2024)
submit(Part2(), session=session_id, day=5, year=2024)