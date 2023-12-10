lines = [[int(x) for x in y.split()] for y in open('input.txt', 'r').read().split('\n')[:-1]]
total = 0

for line in lines:
    firstNumbers = []
    while any([x != 0 for x in line]):
        firstNumbers.append(line[0])
        nextLine = []
        for index, value in enumerate(line[1:]):
            nextLine.append(line[index+1] - line[index])
        line=nextLine
    firstNumbers
    value = 0
    while len(firstNumbers) != 1:
        first = firstNumbers.pop()
        second = firstNumbers.pop()
        firstNumbers.append(second - first)
    total += firstNumbers[0]
print(total)
