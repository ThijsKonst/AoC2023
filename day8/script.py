import re
(instructions, map) = (open('input.txt', 'r').read().split("\n\n"))
instructions = [0 if x == 'L' else 1 for x in instructions]

map = {x[0]: (x[1], x[2]) for x in [re.split("[^a-zA-Z]+", y)
                                    for y in map.split("\n")[:-1]]}
state = 'AAA'
steps = 0
while state != 'ZZZ':
    steps += 1
    instruct = instructions.pop(0)
    instructions.append(instruct)
    state = map[state][instruct]

print(steps)
