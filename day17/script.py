from queue import PriorityQueue
grid = [[int(x) for x in y] for y in open('input.txt', 'r').read().split()]


def prettyPrint(coords):
    for y in range(len(grid)):
        line = ""
        for x in range(len(grid)):
            if (y, x) in coords:
                line += '#'
            else:
                line += str(grid[y][x])
        print(line)


def printPath(path, current):
    totalPath = [(current[0], current[1])]
    total = grid[current[0]][current[1]]
    while current in path:
        current = path[current]
        totalPath += [(current[0], current[1])]
        if (current[0], current[1]) != (0, 0):
            total += grid[current[0]][current[1]]
    print(total)
    prettyPrint(totalPath)
    print(list(reversed(totalPath)))


def h(row, col):
    return len(grid) - row - 1 + len(grid[0]) - col - 1


def neighbors(row, col, previous, count):
    result = []

    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if x + row >= len(grid) or x + row < 0 or y + col >= len(grid) or y+col < 0:
            continue
        if (-x, -y) != previous and not (previous == (x, y) and count == 3):
            newCount = count + 1
            if previous != (x, y):
                newCount = 1
            result.append((row + x, col + y, (x, y), newCount))
    return result


queue = PriorityQueue()
queue.put((0, (0, 0, (0, 0), 0)))
cameFrom = {}
gScore = {(0, 0, (0, 0), 0): 0}
fScore = {(0, 0, (0, 0), 0): h(0, 0)}
visited = []


while queue:
    priority, (row, col, previous, count) = queue.get()
    print(queue.qsize())
    if row == len(grid)-1 and col == len(grid[0])-1:
        print("Done!")
        printPath(cameFrom, (row, col, previous, count))
        break

    nextSteps = neighbors(row, col, previous, count)

    for neighbor in nextSteps:
        tentative_gScore = gScore[(
            row, col, previous, count)] + grid[neighbor[0]][neighbor[1]]
        if tentative_gScore < gScore.get(neighbor, 100000):
            cameFrom[neighbor] = (row, col, previous, count)

            gScore[neighbor] = tentative_gScore
            currentFScore = tentative_gScore + h(neighbor[0], neighbor[1])
            fScore[neighbor] = currentFScore

            if neighbor not in visited:
                visited += [neighbor]
                queue.put((currentFScore, neighbor))
