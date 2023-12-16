file = open("input.txt", 'r').read().split()
fixedRocks, roundRocks = [sum(k, []) for k in zip(*[([(col, row) for col, y in enumerate(x) if y == '#'], [(col, row) for col, y in enumerate(x) if y == 'O'])for row, x in enumerate(file)])]

total = 0

for index, (rockX, rockY) in enumerate(roundRocks):
    for y in range(rockY):
        if (rockX, rockY - y - 1) in fixedRocks or (rockX, rockY - y - 1) in roundRocks:
            roundRocks[index] = (rockX, rockY - y)
            total += len(file) - (rockY - y)
            break
    else:
        roundRocks[index] = (rockX, 0)
        total += len(file)


print(total)
