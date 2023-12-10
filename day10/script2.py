lines = open('testInput.txt', 'r').read().split()
originalLocation = next((index, x.find('S')) for index, x in enumerate(lines) if "S" in x)
currentLocation = originalLocation
paddedMaze = []

paddingConversion = {
    # (north, east, south, west)
    "|": ["A|A", "A|A", "A|A"],
    "-": ["AAA", "---", "AAA"],
    "L": ["A|A", "AL-", "AAA"],
    "J": ["A|A", "-JA", "AAA"],
    "7": ["AAA", "-7A", "A|A"],
    "F": ["AAA", "AF-", "A|A"],
    ".": ["AAA", "A.A", "AAA"],
    "S": ["AAA", "AS-", "A|A"],
}

for rowNum, row in enumerate(lines):
    paddedMaze += ["", "", ""]
    for col in row:
        padding = paddingConversion[col]
        for index, new in enumerate(padding):
            paddedMaze[rowNum*3 + index] += new

for i in paddedMaze:
    print(i)


conversion = {
    # (north, east, south, west)
    "|": (1, 0, 1, 0),
    "-": (0, 1, 0, 1),
    "L": (1, 1, 0, 0),
    "J": (1, 0, 0, 1),
    "7": (0, 0, 1, 1),
    "F": (0, 1, 1, 0),
    ".": (0, 0, 0, 0),
    "S": (1, 1, 1, 1)
}
lines = [[conversion[char] for char in line] for line in lines]
points = set()

def checkOpenings(currentLocation):
    ownOpenings = lines[currentLocation[0]][currentLocation[1]]
    if currentLocation[0] > 0 and lines[currentLocation[0]-1][currentLocation[1]][2] and ownOpenings[0]:
        # go north
        if (currentLocation[0]-1, currentLocation[1]) not in path:
            return (currentLocation[0]-1, currentLocation[1])
    if currentLocation[1] < len(lines[0])-1 and lines[currentLocation[0]][currentLocation[1]+1][3] and ownOpenings[1]:
        # go east
        if (currentLocation[0], currentLocation[1]+1) not in path:
            return (currentLocation[0], currentLocation[1]+1)
    if currentLocation[0] < len(lines)-1 and lines[currentLocation[0]+1][currentLocation[1]][0] and ownOpenings[2]:
        # go south
        if (currentLocation[0]+1, currentLocation[1]) not in path:
            return (currentLocation[0]+1, currentLocation[1])
    if currentLocation[1] > 0 and lines[currentLocation[0]][currentLocation[1]-1][1] and ownOpenings[3]:
        # go west
        if (currentLocation[0], currentLocation[1]-1) not in path:
            return (currentLocation[0], currentLocation[1]-1)
    return originalLocation


count = 0
found = False
path = []

while not found:
    path.append(currentLocation)
    newLocation = checkOpenings(currentLocation)
    currentLocation = newLocation

    count += 1
    
    if currentLocation == originalLocation:
        found = True


def floodFill(location):
    if location[0] not in range(0, len(lines[0])-1) or location[1] not in range(0,len(lines)-1) or lines[currentLocation[0]][currentLocation[1]] == 'B':
        return
    lines[currentLocation[0]][currentLocation[1]] = 'B'
    newLocations = [(x+location[0], y+location[1]) for x in range(-1,2) for y in range(-1,2)]
    for x in newLocations:
        floodFill(x)
print(floodFill((0,0)))
print(count / 2)
