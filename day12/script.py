from itertools import product

lines = [(x.split()[0], [int(k) for k in x.split()[1].split(',')])
         for x in open('input.txt', 'r').readlines()]


def satisfies(input, groups):
    return [len(x) for x in input.split('.') if x != ''] == groups


def applyCheck(input, check):
    for x in range(input.count('?')):
        input = input.replace('?', check.pop(), 1)
    return input


total = 0
possibilities = ['.', '#']
for springs, groups in lines:
    permute = [list(l)
               for l in product(possibilities, repeat=springs.count('?'))]
    new_lines = [applyCheck(springs, check) for check in permute]
    total += len([check for check in new_lines if satisfies(check, groups)])
print(total)
