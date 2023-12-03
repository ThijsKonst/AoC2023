import re
lines = open('input.txt', 'r').readlines()
points = {
    'r': 12,
    'g': 13,
    'b': 14
}


def possible(line):
    games = [x.split(',')
             for x in "".join(line[:-1].split(" ")[2:]).split(';')]
    for game in games:
        for block in game:
            number = re.search(r'\d+', block)
            if int(number.group()) > points[block[number.end()]]:
                return False
    return True


print(sum([index for index, line in enumerate(lines) if possible(line)]))
