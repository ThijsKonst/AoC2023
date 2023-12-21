lines = [list(x) for x in open('input.txt', 'r').read().split()]
start = [(rowIndex, row.index('S'))
         for rowIndex, row in enumerate(lines) if 'S' in row][0]


def neighbors(pos):
    row = pos[0]
    col = pos[1]
    result = []
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if lines[row+x][col+y] != '#':
            result.append((row+x, col+y))
    return result


current = [start]

for x in range(64):
    current = set(sum([neighbors(x) for x in current], []))
print(len(current))
