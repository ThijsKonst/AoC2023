grid = open('input.txt', 'r').read().split()
queue = [(0, 0, "right")]
visited = []
directions = {
    "right": {'|': ['up', 'down'], '\\': ['down'], '/': ['up']},
    "left": {'|': ['up', 'down'], '\\': ['up'], '/': ['down']},
    "up": {'-': ['left', 'right'], '\\': ['left'], '/': ['right']},
    "down": {'-': ['left', 'right'], '\\': ['right'], '/': ['left']}
}
mutations = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while queue:
    row, col, direction = queue.pop()
    if len(grid) <= row or row < 0 or len(grid[0]) <= col or col < 0 or (row, col, direction) in visited:
        continue
    visited.append((row, col, direction))
    char = grid[row][col]
    for instruction in directions[direction].get(char, [direction]):
        rowChange, colChange = mutations[instruction]
        queue.append((row + rowChange, col + colChange, instruction))

visited = {(row, col) for (row, col, direction) in visited}
print(len(set(visited)))
