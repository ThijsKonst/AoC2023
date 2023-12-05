blocks = open('input.txt', 'r').read()[:-1].split('\n\n')
mapping = []

seeds = list(map(int, blocks.pop(0).split()[1:]))

for block in blocks:
    ranges = [list(map(int, x.split()))
              for x in block.split(':\n')[1].split('\n')]

    mapping.append(ranges)


def calculate(seed):
    for convert in mapping:
        for line in convert:
            if line[0] <= seed < line[0] + line[2]:
                seed = line[1] + seed - line[0]
                break
    return seed


print(min([calculate(seed) for seed in seeds]))
