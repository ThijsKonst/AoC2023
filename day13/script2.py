patterns = [[list(y) for y in x.split()]
            for x in open('input.txt', 'r').read().split("\n\n")]


def reflection(pattern):
    for lineNum in range(1, len(pattern)):
        after = pattern[lineNum:min(2*lineNum, len(pattern))]
        before = list(reversed(pattern[max(lineNum - len(after), 0):lineNum]))
        totalDiff = 0

        for index, row in enumerate(after):
            totalDiff += sum(row[i] != before[index][i]
                             for i in range(len(row)))
            if totalDiff > 1:
                break
        if totalDiff == 1:
            return lineNum


total = 0
for pattern in patterns:
    if result := reflection(pattern):
        total += result * 100
    else:
        pattern = list(map(list, zip(*pattern)))
        result = reflection(pattern)
        total += result
print(total)
