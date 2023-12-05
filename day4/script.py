lines = open('input.txt', 'r').readlines()
total = 0

for line in lines:
    (winning, card) = [[int(y) for y in x.split()]
                       for x in line.split(":")[1].split('|')]
    amount = len([num for num in card if num in winning])
    if amount:
        total += pow(2, amount-1)

print(total)
