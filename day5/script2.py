blocks = open('input.txt', 'r').read()[:-1].split('\n\n')
mapping = []

seeds = list(map(int, blocks.pop(0).split()[1:]))
seeds = [(begin, begin + amount)
         for begin, amount in zip(seeds[::2], seeds[1::2])]

for block in blocks:
    ranges = [list(map(int, x.split()))
              for x in block.split(':\n')[1].split('\n')]
    ranges = [((original, original + amount), (new, new + amount))
              for new, original, amount in ranges]
    new_round = []

    for seed in seeds:
        for original, new in ranges:
            amount = new[0] - original[0]
            if seed[0] >= original[1] or seed[1] <= original[0]:
                continue
            changed = (max(seed[0], original[0]),
                       min(seed[1], original[1]))
            if seed[0] < changed[0]:
                seeds.append((seed[0], changed[0]))
            if changed[1] < seed[1]:
                seeds.append((changed[1], seed[1]))
            new_round.append(
                (changed[0] + amount, changed[1] + amount))
            break
        else:
            new_round.append(seed)
    seeds = new_round


print(min([seed[0] for seed in seeds]))
