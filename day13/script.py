patterns = [list(x.split())
            for x in open('input.txt', 'r').read().split("\n\n")]


def reflection(pattern):
    for lineNum in range(1, len(pattern)):
        after = pattern[lineNum:min(2*lineNum, len(pattern))]
        before = list(
            reversed(pattern[max(lineNum - len(after), 0):lineNum]))
        if after == before:
            return lineNum


total = 0
for pattern in patterns:
    for line in pattern:
        print(line)
    if result := reflection(pattern):
        total += result * 100
    else:
        pattern = list(map(list, zip(*pattern)))
        result = reflection(pattern)
        total += result
print(total)
