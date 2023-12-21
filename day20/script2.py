from math import lcm

lines = [(x.strip().split(' -> ')[0], x.strip().split(' -> ')[1].split(', '))
         for x in open('input.txt', 'r').readlines()]


def printLine(input, origin, value):
    print(f"{origin} {'-high' if value else '-low'} -> {input}")


def calculateInputs(key):
    result = {}
    for input, output in lines:
        if key in output:
            result[input[1:]] = False
    return result


flipflops = {x[1:]: (y, False) for x, y in lines if x[0] == '%'}
conjunction = {x[1:]: (y, calculateInputs(x[1:]))
               for x, y in lines if x[0] == '&'}
broadcast = [y for x, y in lines if x == 'broadcaster'][0]


def sendPulse(input, origin, value):
    if input in flipflops and not value:
        flipflops[input] = (flipflops[input][0], not flipflops[input][1])
        return [(x, input, flipflops[input][1]) for x in flipflops[input][0]]
    if input in conjunction:
        relevantCon = conjunction[input]
        relevantCon[1][origin] = value
        if all(relevantCon[1].values()):
            return [(x, input, False) for x in relevantCon[0]]
        return [(x, input, True) for x in relevantCon[0]]
    return []


presses = 0
done = False

memory = {x: 0 for x in calculateInputs(
    [y for y in conjunction if 'rx' in conjunction[y][0]][0])}
print(memory)
while not done:
    presses += 1
    queue = [(x, 'broadcaster', False) for x in broadcast]
    while queue:
        input, origin, value = queue.pop(0)
        if value and input == 'zh':
            print(f"{origin} -> {presses}")
            if not memory[origin]:
                memory[origin] = presses
            if all(memory.values()):
                done = True
                print(lcm(*memory.values()))
                break

        queue += sendPulse(input, origin, value)
