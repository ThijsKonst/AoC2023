lines = [list(x) for x in open('input.txt', 'r').read().split()]
start = [(rowIndex, row.index('S'))
         for rowIndex, row in enumerate(lines) if 'S' in row][0]


def neighbors(pos):
    row = pos[0]
    col = pos[1]
    result = []
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if lines[(row+x) % (len(lines))][(col+y) % (len(lines[0]))] != '#':
            result.append((row+x, col+y))
    return result


def solveSteps(amount):
    print(f"solving for {amount}")
    current = [(start, 0)]
    visited = []
    total = set()
    while current:
        location, steps = current.pop(0)
        if (location, steps) in visited:
            continue
        visited.append((location, steps))
        if steps == amount:
            total.add(location)
            continue
        current += [(x, steps+1) for x in neighbors(location)]
    return len(total)


steps = 26501365
remainder = steps % len(lines[0])
value1 = solveSteps(remainder)
value2 = solveSteps(remainder + len(lines[0]))
value3 = solveSteps(remainder + 2 * len(lines[0]))

a = (value1 - 2 * value2 + value3) / 2
b = (-3 * value1 + 4 * value2 - value3) / 2
c = value1
n = int(steps / len(lines[0]))
result = a * n * n + b * n + c
print(result)
