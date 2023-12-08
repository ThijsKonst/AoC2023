import math
(instructions, map) = (open('input.txt', 'r').read().split("\n\n"))
instructions = [0 if x == 'L' else 1 for x in instructions]

map = {x[0]: x[1].split(', ') for x in [y[:-1].split(' = (')
                                        for y in map.split("\n")[:-1]]}

steps = {x: 0 for x in map.keys() if x.endswith('A')}

for begin in steps.keys():
    currentInstructions = instructions
    state = begin
    while not state.endswith('Z'):
        steps[begin] += 1
        instruct = currentInstructions.pop(0)
        currentInstructions.append(instruct)
        state = map[state][instruct]

print(math.lcm(*steps.values()))
print(steps)
