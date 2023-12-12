from itertools import chain
lines = open("input.txt", 'r').read().split()
coords = list(chain.from_iterable([[(y_index, x_index) for y_index, y in enumerate(x) if y == '#']
                                  for x_index, x in enumerate(lines)]))


empty_cols = []
for x in range(0, len(lines[0])):
    x_axis = [coord[0] for coord in coords]
    if x not in x_axis:
        empty_cols.append(x)

empty_rows = []
for index, y in enumerate(lines):
    if '#' not in y:
        empty_rows.append(index)

coords = [(y + len([k for k in empty_cols if k < y]), x +
           len([k for k in empty_rows if k < x])) for (y, x) in coords]

pairs = []
while len(coords):
    first = coords.pop()
    pairs += [(first, second) for second in coords if first != second]


def distance(start, end):
    return sum(abs(x - y) for x, y in zip(start, end))


print(sum([distance(first, second) for first, second in pairs]))
