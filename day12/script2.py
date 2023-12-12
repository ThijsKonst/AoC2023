from functools import cache

lines = [('?'.join([x.split()[0]]*5), tuple(int(k) for k in x.split()[1].split(',')*5))
         for x in open('input.txt', 'r').readlines()]


@cache
def smartCheck(springs, groups):
    if len(springs) < sum(groups) + len(groups) - 1:
        return 0
    if not len(springs):
        return len(groups) == 0
    first = springs[0]
    if first == '.':
        return smartCheck(springs[1:], groups)
    if first == '?':
        return smartCheck('#'+springs[1:], groups) + smartCheck('.'+springs[1:], groups)
    if first == '#':
        if not len(groups):
            return 0
        length = groups[0]
        firstGroup, springs = springs[:length], springs[length:]
        if '.' in firstGroup:
            return 0
        if springs and springs[0] == '#':
            return 0
        return smartCheck('.'+springs[1:], groups[1:])


print(sum([smartCheck(springs, groups) for springs, groups in lines]))
