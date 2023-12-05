lines = open('input.txt', 'r').readlines()
runningCount = [1] * 10000000
total = 0

for line in lines:
    (winning, card) = [[int(y) for y in x.split()]
                       for x in line.split(":")[1].split('|')]
    cards = runningCount.pop(0)
    amount = len([num for num in card if num in winning])
    runningCount[0:amount] = [x + cards for x in runningCount[0:amount]]
    total += cards

print(total)
