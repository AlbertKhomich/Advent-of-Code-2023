import re
from collections import defaultdict

# Sample input
with open('text.txt', 'r') as file:
    input_data = file.read()

# Parse the input
workflow_data, part_data = input_data.strip().split("\n\n")

# Parse workflows
workflows = {}
for line in workflow_data.splitlines():
    name, rules = line.split("{")
    rules = rules.rstrip("}")
    workflows[name] = []
    for rule in rules.split(","):
        if ":" in rule:
            condition, destination = rule.split(":")
            workflows[name].append((condition, destination))
        else:
            workflows[name].append((None, rule))

# New function to count accepted combinations
def count_accepted(workflow, ranges):
    if workflow == 'A':
        return calculate_combinations(ranges)
    if workflow == 'R':
        return 0

    total = 0
    for condition, destination in workflows[workflow]:
        if condition is None:
            total += count_accepted(destination, ranges)
        else:
            true_ranges, false_ranges = split_range(condition, ranges)
            total += count_accepted(destination, true_ranges)
            ranges = false_ranges
    return total

def split_range(condition, ranges):
    key, op, value = re.match(r"(\w)([<>])?(\d+)", condition).groups()
    value = int(value)
    true_ranges = ranges.copy()
    false_ranges = ranges.copy()
    
    if op == '<':
        true_ranges[key] = (true_ranges[key][0], min(true_ranges[key][1], value - 1))
        false_ranges[key] = (max(false_ranges[key][0], value), false_ranges[key][1])
    elif op == '>':
        true_ranges[key] = (max(true_ranges[key][0], value + 1), true_ranges[key][1])
        false_ranges[key] = (false_ranges[key][0], min(false_ranges[key][1], value))
    
    return true_ranges, false_ranges

def calculate_combinations(ranges):
    result = 1
    for low, high in ranges.values():
        result *= max(0, high - low + 1)
    return result

# Initialize ranges for all ratings
initial_ranges = {key: (1, 4000) for key in 'xmas'}

# Count accepted combinations
total_accepted = count_accepted('in', initial_ranges)
print(total_accepted)