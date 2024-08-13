import re

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

# Parse parts
parts = []
for line in part_data.splitlines():
    part = {}
    for item in line.strip("{}").split(","):
        key, value = item.split("=")
        part[key] = int(value)
    parts.append(part)

# Function to evaluate a condition
def evaluate_condition(condition, part):
    if condition is None:
        return True
    key, op, value = re.match(r"(\w)([<>=]+)(\d+)", condition).groups()
    value = int(value)
    if op == "<":
        return part[key] < value
    elif op == ">":
        return part[key] > value
    elif op == "=":
        return part[key] == value
    return False

# Process each part
total_sum = 0
for part in parts:
    current_workflow = "in"
    while True:
        for condition, destination in workflows[current_workflow]:
            if evaluate_condition(condition, part):
                if destination == "A":
                    total_sum += sum(part.values())
                elif destination == "R":
                    pass
                else:
                    current_workflow = destination
                break
        if destination in ["A", "R"]:
            break

print(total_sum)
