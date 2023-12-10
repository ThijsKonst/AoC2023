import sys

sys.setrecursionlimit(100000)

lines = open('input.txt', 'r').read().split()

paddedMaze = []


paddingConversion = {
    "|": ["A|A", "A|A", "A|A"],
    "-": ["AAA", "---", "AAA"],
    "L": ["A|A", "AL-", "AAA"],
    "J": ["A|A", "-JA", "AAA"],
    "7": ["AAA", "-7A", "A|A"],
    "F": ["AAA", "AF-", "A|A"],
    ".": ["AAA", "A.A", "AAA"],
    "S": ["AAA", "-SA", "A|A"],
}

conversion = {
    # (north, east, south, west)
    "|": (1, 0, 1, 0),
    "-": (0, 1, 0, 1),
    "L": (1, 1, 0, 0),
    "J": (1, 0, 0, 1),
    "7": (0, 0, 1, 1),
    "F": (0, 1, 1, 0),
    ".": (0, 0, 0, 0),
    "S": (1, 1, 1, 1),
    "A": (0, 0, 0, 0),
    "B": (0, 0, 0, 0)
}

for rowNum, row in enumerate(lines):
    paddedMaze += [list(), list(), list()]
    for col in row:
        padding = paddingConversion[col]
        for index, new in enumerate(padding):
            paddedMaze[rowNum*3 + index] += new

paddedMaze = [["B", *x, "B"] for x in paddedMaze]
paddedMaze.insert(0, "B"*len(paddedMaze[0]))
paddedMaze.append("B"*len(paddedMaze[0]))


def checkOpenings(currentLocation):
    ownOpenings = conversion[paddedMaze[currentLocation[0]][currentLocation[1]]]
    if currentLocation[0] > 0 and conversion[paddedMaze[currentLocation[0]-1][currentLocation[1]]][2] and ownOpenings[0]:
        # go north
        if (currentLocation[0]-1, currentLocation[1]) not in path:
            return (currentLocation[0]-1, currentLocation[1])
    if currentLocation[1] < len(paddedMaze[0])-1 and conversion[paddedMaze[currentLocation[0]][currentLocation[1]+1]][3] and ownOpenings[1]:
        # go east
        if (currentLocation[0], currentLocation[1]+1) not in path:
            return (currentLocation[0], currentLocation[1]+1)
    if currentLocation[0] < len(paddedMaze)-1 and conversion[paddedMaze[currentLocation[0]+1][currentLocation[1]]][0] and ownOpenings[2]:
        # go south
        if (currentLocation[0]+1, currentLocation[1]) not in path:
            return (currentLocation[0]+1, currentLocation[1])
    if currentLocation[1] > 0 and conversion[paddedMaze[currentLocation[0]][currentLocation[1]-1]][1] and ownOpenings[3]:
        # go west
        if (currentLocation[0], currentLocation[1]-1) not in path:
            return (currentLocation[0], currentLocation[1]-1)
    return originalLocation

originalLocation = next((index, x.index('S')) for index, x in enumerate(paddedMaze) if "S" in x)
currentLocation = originalLocation

count = 0
found = False
path = []
print("path")

while not found:
    path.append(currentLocation)
    newLocation = checkOpenings(currentLocation)
    paddedMaze[currentLocation[0]][currentLocation[1]] = 'B'
    currentLocation = newLocation

    count += 1
    
    if currentLocation == originalLocation:
        found = True


def floodFill(location):
    currentChar = paddedMaze[location[0]][location[1]]
    if currentChar == 'B':
        return

    paddedMaze[location[0]][location[1]] = 'B'
    newLocations = [(x+location[0], y+location[1]) for x in range(-1,2) for y in range(-1,2)]
    for x in newLocations:
        floodFill(x)

print("floodfill")
floodFill((1,1))


for i in paddedMaze:
    print("".join(i))

points = sum([len([y for y in x if y == '.']) for x in paddedMaze])
rest = sum([len([y for y in x if y not in ['A', 'B', '.']]) for x in paddedMaze])
print(points + rest/3)
