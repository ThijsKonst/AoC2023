lines = [(x.split()[0], int(x.split()[1]))
         for x in open('input.txt', 'r').readlines()]

values = {}

conversion = {
    'T': '10',
    'J': '11',
    'Q': '12',
    'K': '13',
    'A': '14'
}

for hand, bid in lines:
    count = {}
    for char in hand:
        count[char] = count.setdefault(char, 0) + 1
    handKind = tuple(sorted(count.values(), reverse=True))
    hand = [int(conversion.get(key, key)) for key in hand]
    values[handKind] = values.setdefault(handKind, []) + [(hand, bid)]

values = sorted(values.items())
print(sum([z[1]*(index+1) for index, z in enumerate(
    [y for sublist in [sorted(x[1]) for x in values] for y in sublist])]))
