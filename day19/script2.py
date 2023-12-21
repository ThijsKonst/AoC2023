rules, parts = open('input.txt', 'r').read().split("\n\n")

rules = {x.split('{')[0]: x.split('{')[1][:-1].split(',') for x in rules.split()}
rules['A'] = False
rules['R'] = False

def handleRules(rule, input):
    output = []
    currentInput = input
    print(rule)
    for step in rule:
        if ':' not in step:
            output.append((step, currentInput))
            continue
        condition, destination = step.split(':')
        variable = currentInput[condition[0]]
        value = int(condition[2:])
        if condition[1] == '<':
            if variable.start <= value:
                currentInput[condition[0]] = range(variable.start, value)
            output.append((destination, dict(currentInput)))
            currentInput[condition[0]] = range(value, variable.stop)
            continue
        if condition[1] == '>':
            if value <= variable.stop:
                currentInput[condition[0]] = range(value+1, variable.stop)
            output.append((destination, dict(currentInput)))
            currentInput[condition[0]] = range(variable.start, value + 1)
            continue
    print(output)
    print([len(input['x']) * len(input['m']) * len(input['a']) * len(input['s']) for key, input in output])
    return output

total = 0

queue = [('in', {'x': range(1, 4001), 'm': range(1, 4001), 'a': range(1, 4001), 's': range(1, 4001)})]
while queue:
    rule, input = queue.pop()
    if rule == 'R':
        continue
    if rule == 'A':
        total += len(input['x']) * len(input['m']) * len(input['a']) * len(input['s'])
        continue
    queue += handleRules(rules[rule], input)


print(total)
