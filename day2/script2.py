import re
from functools import reduce
import operator
lines = open('input.txt', 'r').readlines()


def power(line):
    games = "".join(line[:-1].split(" ")[2:]).replace(';', ',').split(',')
    print(games)
    power = {}
    for game in games:
        number = re.search(r'\d+', game)
        if int(number.group()) > power.get(game[-1], 0):
            power[game[-1]] = int(number.group())
    return reduce(operator.mul, power.values())


print(sum([power(line) for line in lines]))
