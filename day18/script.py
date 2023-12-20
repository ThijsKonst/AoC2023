lines = [(x.split()[0], int(x.split()[1]), x.split()[2][1:-1])
         for x in open('input.txt', 'r').readlines()]

current = (0, 0)
convert = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}
coords = []


def prettyPrint(coords):
    for y in range(max([k[0] for k in coords])+1):
        line = ""
        for x in range(max([k[1] for k in coords])+1):
            if (y, x) in coords:
                line += '#'
            else:
                line += '.'
        print(line)


def floodFill(start, coords):
    queue = [start]
    visited = []
    total = 0
    print(coords)
    borderRow, borderCol = (
        max([x[0] for x in coords]), max([x[1] for x in coords]))
    while queue:
        location = queue.pop()
        visited.append(location)
        total += 1
        if location in coords:
            continue

        newLocations = [(x+location[0], y+location[1])
                        for x in range(-1, 2) for y in range(-1, 2) if 0 <= x+location[0] < borderRow and 0 <= y+location[1] < borderCol]

        queue += [x for x in newLocations if x not in queue and x not in visited]
    return total


def normalize(coords):
    rowLowerBound = min([x[0] for x in coords])
    colLowerBound = min([x[1] for x in coords])
    return [(x-rowLowerBound, y-colLowerBound) for x, y in coords]


for direction, amount, color in lines:
    mutation = convert[direction]
    for amount in range(amount):
        coords.append(current)
        current = tuple(map(sum, zip(current, mutation)))
# prettyPrint(coords)
coords = normalize(coords)
average = (int(sum([x[0] for x in coords])/len(coords)),
           int(sum([x[1] for x in coords])/len(coords)))
print(floodFill(average, coords))
