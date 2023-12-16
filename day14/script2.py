file = open("input.txt", 'r').read().split()
fixedRocks, roundRocks = [sum(k, []) for k in zip(*[([(col, row) for col, y in enumerate(x) if y == '#'], [(col, row) for col, y in enumerate(x) if y == 'O'])for row, x in enumerate(file)])]

def rotate(rocks):
    newRocks = [] 
    for (x, y) in rocks:
        newRocks.append((99 - y, x))
    return newRocks

def prettyPrint(roundRocks, fixedRocks):
    for y in range(100):
        line = ""
        for x in range(100):
            if (x, y) in fixedRocks:
                line += '#'
            elif (x, y) in roundRocks:
                line += 'O'
            else:
                line += '.'
        print(line)

def tilt(roundRocks, fixedRocks):
    newRoundRocks = []
    for rockX, rockY in roundRocks:
        relevantRocks = [x[1] for x in fixedRocks if x[0] == rockX]
        found = 0
        for rock in relevantRocks:
            if found <= rock < rockY:
                found = rock + 1
        while (rockX, found) in newRoundRocks:
            found = found + 1
        newRoundRocks.append((rockX, found))

    return newRoundRocks, fixedRocks

def cycle(roundRocks, fixedRocks):
    for x in range(4):
        roundRocks, fixedRocks = tilt(roundRocks, fixedRocks)
        roundRocks, fixedRocks = rotate(roundRocks), rotate(fixedRocks)
    return roundRocks, fixedRocks



visitedRocks = {}
iteration = 0
while iteration <= 1000000000:
    roundRocks, fixedRocks = cycle(roundRocks, fixedRocks)
    roundRocks = tuple(sorted(roundRocks))
    iteration += 1
    print(iteration)
    if roundRocks in visitedRocks:
        period = iteration - visitedRocks[roundRocks]
        skipped = int((1000000000 - iteration) / period)
        iteration += skipped * period
        print(iteration)
    visitedRocks[roundRocks] = iteration


prettyPrint(roundRocks, fixedRocks)
print("---------")
print(sum([len(file) - x[1] for x in roundRocks]))
