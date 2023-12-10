lines = [[int(x) for x in y.split()] for y in open('input.txt', 'r').read().split('\n')[:-1]]
total = 0

for line in lines:
    lastNumbers = []
    while any([x != 0 for x in line]):
        lastNumbers.append(line[-1])
        nextLine = []
        for index, value in enumerate(line[:-1]):
            nextLine.append(line[index+1] - line[index])
        line=nextLine
    total += sum(lastNumbers)
print(total)
