from queue import PriorityQueue
grid = [[int(x) for x in y] for y in open('testInput.txt', 'r').read().split()]


def prettyPrint(coords):
    for y in range(len(grid)):
        line = ""
        for x in range(len(grid)):
            if (y, x) in coords:
                line += '#'
            else:
                line += str(grid[y][x])
        print(line)


def printPath(path, row, col):
    totalPath = [(row, col)]
    total = 0
    changes = []
    while (row, col) in path:
        row, col, change = path[(row, col)]
        changes += [change]
        totalPath += [(row, col)]
        total += grid[row][col]
    print(total)
    prettyPrint(totalPath)
    print(list(reversed(changes)))
    print(list(reversed(totalPath)))


def h(row, col):
    return len(grid) - row - 1 + len(grid[0]) - col - 1


queue = PriorityQueue()
queue.put((0, (0, 0, [])))
cameFrom = {}
gScore = {(0, 0): 0}
fScore = {(0, 0): h(0, 0)}
visited = []


while queue:
    priority, (row, col, previous) = queue.get()
    if row == len(grid)-1 and col == len(grid[0])-1:
        printPath(cameFrom, row, col)
        break

    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if previous:
        neighbors = [(x, y) for x, y in neighbors if (-x, -y) !=
                     previous[0] and previous.count((x, y)) != 3]

    for changeRow, changeCol in neighbors:
        checkRow, checkCol = (changeRow + row, changeCol + col)

        if checkRow >= len(grid) or checkRow < 0 or checkCol >= len(grid[0]) or checkCol < 0:
            continue

        tentative_gScore = gScore[(row, col)] + grid[checkRow][checkCol]
        if tentative_gScore < gScore.get((checkRow, checkCol), 100000):

            cameFrom[(checkRow, checkCol)] = (row, col, (changeRow, changeCol))

            gScore[(checkRow, checkCol)] = tentative_gScore
            currentFScore = tentative_gScore + h(checkRow, checkCol)
            fScore[(checkRow, checkCol)] = currentFScore

            if (checkRow, checkCol, previous) not in visited:
                visited += [(checkRow, checkCol, previous)]
                queue.put(
                    (currentFScore, (checkRow, checkCol, [(changeRow, changeCol)] + previous[:2])))
