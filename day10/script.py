lines = open('input.txt', 'r').read().split()
found = False
originalLocation = next((index, x.find('S')) for index, x in enumerate(lines) if "S" in x)
currentLocation = originalLocation

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

def checkOpenings(currentLocation):
    ownOpenings = lines[currentLocation[0]][currentLocation[1]]
    if currentLocation[0] > 0 and lines[currentLocation[0]-1][currentLocation[1]][2] and ownOpenings[0]:
        return (currentLocation[0] - 1, currentLocation[1])
    if currentLocation[1] < len(lines[0]) -1 and lines[currentLocation[0]][currentLocation[1]+1][3] and ownOpenings[1]:
        return (currentLocation[0], currentLocation[1]+1)
    if currentLocation[0] < len(lines) -1 and lines[currentLocation[0]+1][currentLocation[1]][0] and ownOpenings[2]:
        return (currentLocation[0]+1, currentLocation[1])
    if currentLocation[1] > 0 and lines[currentLocation[0]][currentLocation[1]-1][1] and ownOpenings[3]:
        return (currentLocation[0], currentLocation[1]-1)
    return originalLocation


count = 0
while not found:
    newLocation = checkOpenings(currentLocation)
    lines[currentLocation[0]][currentLocation[1]] = (0, 0, 0, 0)
    currentLocation = newLocation
    count += 1
    
    if currentLocation == originalLocation:
        found = True
print(count / 2)
