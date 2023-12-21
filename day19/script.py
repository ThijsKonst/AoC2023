rules, parts = open('input.txt', 'r').read().split("\n\n")

rules = {x.split('{')[0]: x.split('{')[1][:-1].split(',') for x in rules.split()}
rules['A'] = False
rules['R'] = False
parts = [{y[0]: int(y[2:]) for y in x[1:-1].split(',')} for x in parts.split()]

def handleRule(part, rule):
    if ':' not in rule:
        return rule
    condition, destination = rule.split(':')
    variable = part[condition[0]]
    value = int(condition[2:])
    if condition[1] == '>' and variable > value:
        return destination
    if condition[1] == '<' and variable < value:
        return destination
    return False

total = 0

for part in parts:
    next = rules['in']
    while next:
        for rule in next:
            result = handleRule(part, rule)
            if result == 'A':
                total += sum(part.values())
            if result:
                next = rules[result]
                break

print(total)
